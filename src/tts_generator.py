"""
edge-tts 기반 한국어 성우 + 미국 프리미엄 원어민 성우 듀얼 음성 및 획별 획순 가이드 음성 자동 생성 모듈
- 한자별 정확한 획 명칭(가로, 세로, 삐침, 파임 등) 음성 지원
- 고급스럽고 자연스러운 프리미엄 미국 영문 내레이션 (en-US-AriaNeural)
- 슬래시(/) 등 특수문자를 자연스러운 쉼표 및 호흡으로 처리하여 '슬래시' 발음 원천 차단
"""
import os
import sys
import re
import asyncio
import edge_tts
import subprocess

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 한국어 성우 (밝고 또렷한 톤)
VOICE_KO = "ko-KR-SunHiNeural"
# 미국 원어민 고급 성우 (자연스럽고 세련된 프리미엄 내레이션)
VOICE_EN = "en-US-AriaNeural"

def clean_spoken_text(text: str) -> str:
    """TTS 음성 낭독 시 슬래시(/)나 불필요한 기호를 자연스러운 쉼표로 변환"""
    if not text:
        return ""
    # 슬래시 및 괄호 처리
    text = text.replace("/", ", ").replace("  ", " ").strip()
    return text

async def generate_speech_async(text: str, output_path: str, voice: str = VOICE_KO, rate: str = "+0%", pitch: str = "+0Hz", volume: str = "+25%"):
    """텍스트를 고품질 신경망 음성 파일(mp3)로 생성 (볼륨 증폭 지원)"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    clean_text = clean_spoken_text(text)
    communicate = edge_tts.Communicate(clean_text, voice, rate=rate, pitch=pitch, volume=volume)
    await communicate.save(output_path)
    print(f"[TTS ({voice})] Generated: {output_path} -> \"{clean_text}\"")

def generate_speech(text: str, output_path: str, voice: str = VOICE_KO, rate: str = "+0%", pitch: str = "+0Hz", volume: str = "+25%"):
    """동기식 래퍼 함수"""
    asyncio.run(generate_speech_async(text, output_path, voice, rate, pitch, volume))

def prepare_hanzi_audios(hanzi_info: dict, base_dir: str = "assets/audio"):
    """한자 항목에 필요한 한국어/원어민 영어 듀얼 오디오 및 획별 가이드 음성 일괄 생성"""
    char = hanzi_info["char"]
    char_audio_dir = os.path.join(base_dir, f"char_{char}")
    os.makedirs(char_audio_dir, exist_ok=True)

    # 1. 훅 오디오 (한국어) - 시작 부분 귀에 쏙 들어오도록 크고 또렷하게
    hook_path = os.path.join(char_audio_dir, "hook.mp3")
    generate_speech(f"{hanzi_info['sound_desc']}!", hook_path, voice=VOICE_KO, rate="+10%", pitch="+2Hz", volume="+35%")

    # 2. 획별 획순 가이드 음성 생성 (한자 데이터베이스의 정확한 획 명칭 적용)
    stroke_names_list = hanzi_info.get("stroke_names", [])
    
    stroke_audios = []
    for order in range(1, hanzi_info["stroke_count"] + 1):
        if stroke_names_list and len(stroke_names_list) >= order:
            s_text = stroke_names_list[order - 1]
        else:
            s_text = f"{order}번째 획!"
            
        s_path = os.path.join(char_audio_dir, f"stroke_{order}_guide.mp3")
        generate_speech(s_text, s_path, voice=VOICE_KO, rate="+15%", pitch="+3Hz", volume="+25%")
        stroke_audios.append(s_path)

    # 3. 훈음 파트: [한국어] "큰 대!" + [미국 원어민] "Big, Great."
    huneum_ko_path = os.path.join(char_audio_dir, "huneum_ko.mp3")
    huneum_en_path = os.path.join(char_audio_dir, "huneum_en.mp3")
    combined_huneum_path = os.path.join(char_audio_dir, "huneum_combined.mp3")

    generate_speech(f"{hanzi_info['hun_eum']}!", huneum_ko_path, voice=VOICE_KO, rate="+5%", pitch="+2Hz", volume="+30%")
    # 슬래시 제거된 영문 훈음
    clean_en_huneum = clean_spoken_text(hanzi_info['hun_eum_en'])
    generate_speech(f"{clean_en_huneum}.", huneum_en_path, voice=VOICE_EN, rate="+0%", volume="+25%")

    # 한국어 + 영어 순차 연결
    concat_cmd_1 = [
        "ffmpeg", "-y",
        "-i", huneum_ko_path,
        "-i", huneum_en_path,
        "-filter_complex", "[0:0][1:0]concat=n=2:v=0:a=1[out]",
        "-map", "[out]",
        combined_huneum_path
    ]
    subprocess.run(concat_cmd_1, capture_output=True)

    # 4. 단어 파트: [한국어] "대인! 마음이 넓고 훌륭한 사람." + [미국 원어민] "Adult, Great person."
    word_ko_path = os.path.join(char_audio_dir, "word_ko.mp3")
    word_en_path = os.path.join(char_audio_dir, "word_en.mp3")
    combined_word_path = os.path.join(char_audio_dir, "word_combined.mp3")

    clean_word_ko = hanzi_info['example_word'].split('(')[-1].replace(')', '').strip()
    ko_desc = hanzi_info['example_word_desc'].split('(')[0].strip()
    generate_speech(f"{clean_word_ko}! {ko_desc}.", word_ko_path, voice=VOICE_KO, rate="+5%", volume="+25%")
    
    # 괄호 안의 영어 텍스트만 깔끔하게 추출하여 슬래시 제거 후 낭독
    en_desc = hanzi_info['example_word_desc']
    if '(' in en_desc and ')' in en_desc:
        raw_en_word = en_desc.split('(')[-1].replace(')', '').strip()
    else:
        raw_en_word = hanzi_info['hun_eum_en']
    
    clean_en_word = clean_spoken_text(raw_en_word)
    generate_speech(f"{clean_en_word}.", word_en_path, voice=VOICE_EN, rate="+0%", volume="+25%")

    concat_cmd_2 = [
        "ffmpeg", "-y",
        "-i", word_ko_path,
        "-i", word_en_path,
        "-filter_complex", "[0:0][1:0]concat=n=2:v=0:a=1[out]",
        "-map", "[out]",
        combined_word_path
    ]
    subprocess.run(concat_cmd_2, capture_output=True)

    return {
        "hook": hook_path,
        "strokes": stroke_audios,
        "huneum": combined_huneum_path if os.path.exists(combined_huneum_path) else huneum_ko_path,
        "example_word": combined_word_path if os.path.exists(combined_word_path) else word_ko_path
    }

if __name__ == "__main__":
    from hanzi_data import HANZI_DATABASE
    res = prepare_hanzi_audios(HANZI_DATABASE["大"])
    print("Prepared audio files:", res)
