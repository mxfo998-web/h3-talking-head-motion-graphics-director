#!/usr/bin/env python3
"""Structural lint for H3 talking-head VFX prompts."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BASE_FIELDS = [
    "integrated_multimodal_description:",
    "overall_soundscape:",
    "non_diegetic_music:",
]

REF_FIELDS = [
    "subject_definitions:",
    "summary:",
    "retention_analysis:",
    "detailed_description:",
    "overall_soundscape:",
    "non_diegetic_music:",
]

RUNTIME_FORBIDDEN = [
    (r"<Audio\s+\d+>", "runtime-audio-label", "Runtime driver must not receive an <Audio N> label."),
    (r"\baudio reuse\b", "runtime-audio-reuse", "Runtime driver must not add audio reuse."),
    (r"\baudio reference\b", "runtime-audio-reference", "Runtime driver must not add audio reference."),
    (r"\b(?:fully_copy|partially_copy|weak_reference)\b", "runtime-audio-retention", "Runtime driver must not receive audio retention markers."),
    (r"参考音频\s*\d+|复制音频\s*\d+|沿用\s*<Audio", "runtime-audio-wording", "Runtime driver must not be described as a numbered reference audio."),
]

EFFECT_TRIGGER_TERMS = r"触发|说到|重音|同步|trigger|semantic|lands? on"
EFFECT_ENTRANCE_TERMS = r"出现|进入|淡入|显现|展开|组装|绘制|上升|弹出|亮起|reveal|enter|fade in|draw on|unfold|materiali[sz]e"
EFFECT_EXIT_TERMS = r"完全消失|退出|退场|淡出|折叠|收回|缩回|溶解|反向擦除|变形为|恢复干净|exit|fade out|collapse|retract|dissolve|recover|morph into"
HUMAN_GAZE_TERMS = r"镜头|注视|视线|眼神|gaze|lens|attention target"
HUMAN_MOUTH_TERMS = r"音素|辅音|元音|闭唇|口型|嘴唇|下颌|phoneme|lip|jaw"
HUMAN_BREATH_TERMS = r"呼吸|吸气|呼气|换气|吞咽|breath|inhale|exhale|swallow"
HUMAN_RECOVERY_TERMS = r"回到休息|回看镜头|姿态释放|部分释放|回落|恢复|resting state|partial release|recover"


def ordered(text: str, fields: list[str]) -> bool:
    positions = [text.find(field) for field in fields]
    return all(position >= 0 for position in positions) and positions == sorted(positions)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", type=Path)
    parser.add_argument("--mode", required=True, choices=["T2VA", "I2VA", "FL2VA", "L2VA", "Ref2VA"])
    parser.add_argument("--runtime-audio", action="store_true")
    parser.add_argument("--audio-mode", choices=["runtime", "reference", "generated"])
    parser.add_argument("--duration-seconds", type=float)
    parser.add_argument("--target-cps", type=float, default=5.0)
    args = parser.parse_args()

    text = args.prompt.read_text(encoding="utf-8")
    errors: list[tuple[str, str]] = []
    warnings: list[tuple[str, str]] = []

    dialogue_spans = re.findall(r"<d>\[[^\]]+\]\s*(.*?)</d>", text, re.I | re.S)
    speech_chars = sum(len(re.sub(r"\s+", "", span)) for span in dialogue_spans)
    if dialogue_spans:
        if not re.search(r"(?:字|字符)\s*/?\s*秒|characters? per second|chars?/?s", text, re.I):
            warnings.append(("speech-rate", "State the intended speaking rate for exact dialogue."))
        if args.duration_seconds:
            target_chars = args.duration_seconds * args.target_cps
            tolerance = max(5.0, target_chars * 0.10)
            if abs(speech_chars - target_chars) > tolerance:
                warnings.append(("speech-budget", f"Dialogue has {speech_chars} written characters; target is about {target_chars:.0f} at {args.target_cps:g} chars/s for {args.duration_seconds:g}s."))

    fields = REF_FIELDS if args.mode == "Ref2VA" else BASE_FIELDS
    if not ordered(text, fields):
        errors.append(("field-order", f"Expected fields in order: {' -> '.join(fields)}"))

    if args.mode == "Ref2VA" and "integrated_multimodal_description:" in text:
        errors.append(("mixed-schema", "Ref2VA must not include the Base-mode integrated field."))
    if args.mode != "Ref2VA" and "subject_definitions:" in text:
        errors.append(("mixed-schema", "Base mode must not include Ref2VA subject definitions."))

    if args.mode == "I2VA" and not re.search(r"(?:完全一致|exact).{0,24}(?:首帧|first frame)", text, re.I | re.S):
        errors.append(("first-frame", "I2VA must state exact first-frame alignment."))

    audio_mode = args.audio_mode or ("runtime" if args.runtime_audio else None)
    if args.runtime_audio and args.audio_mode and args.audio_mode != "runtime":
        errors.append(("audio-mode-conflict", "--runtime-audio conflicts with the selected --audio-mode."))

    if audio_mode == "runtime":
        for pattern, code, message in RUNTIME_FORBIDDEN:
            if re.search(pattern, text, re.I):
                errors.append((code, message))
        if not re.search(r"平台运行时驱动音频|输入驱动语音|驱动语音|runtime driving", text, re.I):
            warnings.append(("runtime-binding", "State how the runtime driver controls mouth, breath, performance, and effects."))

    if audio_mode == "generated":
        if re.search(r"<Audio\s+\d+>|参考音频\s*\d+|平台运行时驱动音频|runtime driving", text, re.I):
            errors.append(("generated-audio-reference", "Generated-voice mode must not invent an audio reference or runtime driver."))
        generated_voice_checks = [
            (r"成年女声|成年男声|中性声线|adult female voice|adult male voice|neutral voice", "generated-voice-presentation", "State adult female, adult male, or neutral voice presentation."),
            (r"听感约|年龄感|青年|中年|adult|vocal age", "generated-voice-age", "State apparent vocal age or age band."),
            (r"音高|中低音|中音|中高音|低音|pitch", "generated-voice-pitch", "State pitch region or range."),
            (r"共鸣|声线|音色|质感|resonance|timbre|texture", "generated-voice-timbre", "State resonance, vocal weight, or restrained texture."),
            (r"节奏|停顿|重音|句尾|语调|cadence|pause|stress|intonation", "generated-voice-prosody", "State cadence, pauses, emphasis, or sentence-final contour."),
            (r"领夹|桌面麦克风|吊杆|话筒|近场|收音|麦克风|lavalier|boom|microphone", "generated-voice-mic", "State microphone perspective and distance."),
            (r"室内|房间|空间|混响|底噪|环境声|room tone|reflection|reverb|ambience", "generated-voice-room", "State room tone, reflections, or environmental bleed."),
            (r"播音|销售|客服|预告片|单调|机械|TTS|vocoder|metallic|announcer|sales", "generated-voice-antistyle", "State the likely synthetic or genre voice failure to avoid."),
        ]
        for pattern, code, message in generated_voice_checks:
            if not re.search(pattern, text, re.I):
                warnings.append((code, message))

    if not re.search(r"\[Shot\s+1\]", text, re.I):
        errors.append(("shot-1", "Prompt must contain [Shot 1]."))

    if re.search(r"[\"“][^\"”]+[\"”]", text):
        stability_terms = r"稳定|字形|字序|拼写|标点|不漂移|不乱码|stable|spelling|glyph"
        if not re.search(stability_terms, text, re.I):
            warnings.append(("text-stability", "Visible copy is quoted but no glyph/spelling stability clause was found."))

    if re.search(r"特效|文字|图标|面板|card|icon|effect", text, re.I):
        if not re.search(EFFECT_TRIGGER_TERMS, text, re.I):
            warnings.append(("semantic-trigger", "Bind effects to an exact phrase, semantic beat, or audible event."))
        if not re.search(r"保持|停留|hold|readable", text, re.I):
            warnings.append(("readable-hold", "Give primary information a readable hold state."))
        if not re.search(r"恢复|回落|退出|消失|settle|exit|recover", text, re.I):
            warnings.append(("effect-recovery", "Give effects a settle, exit, or recovery state."))
        if not re.search(r"遮挡|安全区|safe|occlu", text, re.I):
            warnings.append(("safe-placement", "Protect faces, mouths, hands, products, subtitles, and safe areas."))

        effect_blocks = [
            block.strip()
            for block in re.split(r"\n\s*\n", text)
            if re.search(EFFECT_TRIGGER_TERMS, block, re.I)
            and re.search(EFFECT_ENTRANCE_TERMS, block, re.I)
            and re.search(r"特效|文字|图标|面板|卡片|节点|图形|模型|UI|HUD|FUI|全息|card|icon|panel|effect|graphic", block, re.I)
            and not re.search(r"真人表演|口型(?:严格|逐|按)|human performance|phoneme-level mouth", block, re.I)
        ]
        unpaired_blocks = [
            index + 1
            for index, block in enumerate(effect_blocks)
            if not re.search(EFFECT_EXIT_TERMS, block, re.I)
        ]
        if unpaired_blocks:
            warnings.append((
                "unpaired-effect-exit",
                f"{len(unpaired_blocks)} triggered effect block(s) introduce graphics without an explicit observable exit and clean recovery.",
            ))

        entrance_count = len(re.findall(EFFECT_ENTRANCE_TERMS, text, re.I))
        exit_count = len(re.findall(EFFECT_EXIT_TERMS, text, re.I))
        if entrance_count >= 3 and exit_count <= 1:
            warnings.append((
                "effect-accumulation-risk",
                "Several entrances appear to rely on one global cleanup. Pair each independent group with its own in-clip exit or morph transition.",
            ))

    if re.search(r"人物|口播|主持|说话|speaker|presenter|talking", text, re.I):
        if not re.search(HUMAN_GAZE_TERMS, text, re.I):
            warnings.append(("human-gaze", "Name the speaker's attention target and any motivated gaze return."))
        if not re.search(HUMAN_MOUTH_TERMS, text, re.I):
            warnings.append(("human-mouth", "Bind mouth and jaw behavior to actual phonemes and silence."))
        if not re.search(HUMAN_BREATH_TERMS, text, re.I):
            warnings.append(("human-breath", "Describe phrase-linked breathing or breath recovery."))
        if not re.search(HUMAN_RECOVERY_TERMS, text, re.I):
            warnings.append(("human-recovery", "Give gaze, expression, posture, and gestures an observable recovery or resting state."))
        if not re.search(r"眨眼|blink", text, re.I):
            warnings.append(("human-blink", "Place contextual non-periodic blinks near breaths, gaze shifts, or phrase boundaries."))
        if not re.search(r"手势|手部|手掌|左手|右手|双手|gesture|hand", text, re.I):
            warnings.append(("human-gesture", "Specify a motivated gesture or explicit resting hand state."))

    if re.search(r"频闪|闪烁|strobe|flash", text, re.I) and not re.search(r"不超过.{0,8}3|少于.{0,8}3|避免|禁止|不出现|below.{0,8}three", text, re.I):
        warnings.append(("flash-safety", "Confirm that flashing stays below three flashes per second and avoids large saturated-red flashes."))

    if len(text) > 7000:
        warnings.append(("prompt-length", f"Prompt is {len(text)} characters; verify the active platform limit and simplify if needed."))

    pace_note = f" speech_chars={speech_chars}" if dialogue_spans else ""
    if dialogue_spans and args.duration_seconds:
        pace_note += f" target_speech_chars={args.duration_seconds * args.target_cps:.0f}"
    audio_note = f" audio_mode={audio_mode}" if audio_mode else ""
    print(f"valid={not errors} mode={args.mode}{audio_note} chars={len(text)}{pace_note}")
    for code, message in errors:
        print(f"error {code}: {message}")
    for code, message in warnings:
        print(f"warning {code}: {message}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
