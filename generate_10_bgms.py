"""
100만 유튜버 감성 한자 학습 BGM 10곡 전문 생성기 (획순 쓰기 구간 클린 음소거 최적화)
- [0s ~ 3.5s 상형 훅 인트로]: 시선을 사로잡는 영롱하고 통통 튀는 멜로디
- [3.5s ~ 13.0s 붓글씨 획순 쓰기]: 붓 마찰음(ASMR)과 가이드 음성에 100% 집중할 수 있도록 배경음악 완전 배제/음소거
- [13.0s ~ 35.0s 훈음/단어 아웃트로]: 글자 완성 축하 차임 & 따뜻하고 감미로운 어쿠스틱 여운
"""
import os
import sys
import wave
import numpy as np

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

SAMPLE_RATE = 44100
DURATION = 35.0  # 숏폼 최적 재생 시간 (35초)

def get_frequencies():
    notes = {
        "C3": 130.81, "D3": 146.83, "E3": 164.81, "F3": 174.61, "G3": 196.00, "A3": 220.00, "B3": 246.94,
        "C4": 261.63, "D4": 293.66, "E4": 329.63, "F4": 349.23, "G4": 392.00, "A4": 440.00, "B4": 493.88,
        "C5": 523.25, "D5": 587.33, "E5": 659.25, "F5": 698.46, "G5": 783.99, "A5": 880.00, "B5": 987.77,
        "C6": 1046.50, "D6": 1174.66, "E6": 1318.51, "G6": 1567.98, "A6": 1760.00
    }
    return notes

# -------------------------------------------------------------
# 음색 합성 엔진 (Synthesizers)
# -------------------------------------------------------------
def synth_marimba(freq, duration, amp):
    n_samples = int(duration * SAMPLE_RATE)
    t = np.linspace(0, duration, n_samples, endpoint=False)
    env = np.exp(-t * 9.0) * (1.0 - np.exp(-t * 350.0))
    body = (
        1.00 * np.sin(2 * np.pi * freq * t) +
        0.40 * np.sin(2 * np.pi * (freq * 4.0) * t) * np.exp(-t * 24.0) +
        0.15 * np.sin(2 * np.pi * (freq * 10.0) * t) * np.exp(-t * 60.0)
    )
    click = np.random.uniform(-0.15, 0.15, n_samples) * np.exp(-t * 300.0)
    return (body + click) * env * amp

def synth_kalimba(freq, duration, amp):
    n_samples = int(duration * SAMPLE_RATE)
    t = np.linspace(0, duration, n_samples, endpoint=False)
    env = np.exp(-t * 4.5) * (1.0 - np.exp(-t * 220.0))
    tine = (
        1.00 * np.sin(2 * np.pi * freq * t) +
        0.48 * np.sin(2 * np.pi * (freq * 2.98) * t) * np.exp(-t * 8.0) +
        0.22 * np.sin(2 * np.pi * (freq * 5.92) * t) * np.exp(-t * 16.0)
    )
    ping = np.random.uniform(-0.1, 0.1, n_samples) * np.exp(-t * 200.0)
    return (tine + ping) * env * amp

def synth_pizzicato(freq, duration, amp):
    n_samples = int(duration * SAMPLE_RATE)
    t = np.linspace(0, duration, n_samples, endpoint=False)
    env = np.exp(-t * 12.0) * (1.0 - np.exp(-t * 400.0))
    pluck = (
        1.00 * np.sin(2 * np.pi * freq * t) +
        0.70 * np.sin(2 * np.pi * (freq * 2.0) * t) * np.exp(-t * 16.0) +
        0.45 * np.sin(2 * np.pi * (freq * 3.0) * t) * np.exp(-t * 24.0)
    )
    return pluck * env * amp

def synth_musicbox(freq, duration, amp):
    n_samples = int(duration * SAMPLE_RATE)
    t = np.linspace(0, duration, n_samples, endpoint=False)
    env = np.exp(-t * 3.2) * (1.0 - np.exp(-t * 250.0))
    tone = (
        1.00 * np.sin(2 * np.pi * freq * t) +
        0.55 * np.sin(2 * np.pi * (freq * 2.0) * t) +
        0.25 * np.sin(2 * np.pi * (freq * 3.0) * t)
    )
    return tone * env * amp

def synth_piano(freq, duration, amp):
    n_samples = int(duration * SAMPLE_RATE)
    t = np.linspace(0, duration, n_samples, endpoint=False)
    env = np.exp(-t * 2.2) * (1.0 - np.exp(-t * 150.0))
    tone = (
        1.00 * np.sin(2 * np.pi * freq * t) +
        0.50 * np.sin(2 * np.pi * (freq * 2.0) * t) * np.exp(-t * 3.0) +
        0.25 * np.sin(2 * np.pi * (freq * 3.0) * t) * np.exp(-t * 5.0)
    )
    return tone * env * amp

def synth_gayageum(freq, duration, amp):
    n_samples = int(duration * SAMPLE_RATE)
    t = np.linspace(0, duration, n_samples, endpoint=False)
    vibrato = 1.0 + 0.008 * np.sin(2 * np.pi * 5.0 * t)
    env = np.exp(-t * 5.0) * (1.0 - np.exp(-t * 280.0))
    tone = (
        1.00 * np.sin(2 * np.pi * freq * vibrato * t) +
        0.60 * np.sin(2 * np.pi * (freq * 2.0) * t) * np.exp(-t * 8.0) +
        0.35 * np.sin(2 * np.pi * (freq * 3.0) * t) * np.exp(-t * 14.0)
    )
    return tone * env * amp

def synth_crystal_bell(freq, duration, amp):
    n_samples = int(duration * SAMPLE_RATE)
    t = np.linspace(0, duration, n_samples, endpoint=False)
    env = np.exp(-t * 1.8) * (1.0 - np.exp(-t * 120.0))
    tone = (
        1.00 * np.sin(2 * np.pi * freq * t) +
        0.65 * np.sin(2 * np.pi * (freq * 1.5) * t) * np.exp(-t * 2.5) +
        0.40 * np.sin(2 * np.pi * (freq * 2.0) * t) * np.exp(-t * 3.5)
    )
    shimmer = 1.0 + 0.1 * np.sin(2 * np.pi * 6.0 * t)
    return tone * shimmer * env * amp


def save_wav(filename, audio):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # 페이드 인/아웃
    fade_in = int(0.25 * SAMPLE_RATE)
    fade_out = int(2.5 * SAMPLE_RATE)
    if len(audio) > fade_in + fade_out:
        audio[:fade_in] *= np.linspace(0, 1, fade_in)
        audio[-fade_out:] *= np.linspace(1, 0, fade_out)
    
    # 노멀라이즈 (-1.0dB)
    max_val = np.max(np.abs(audio))
    if max_val > 0:
        audio = audio / max_val * 0.88
    
    audio_int16 = (audio * 32767).astype(np.int16)
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(audio_int16.tobytes())
    print(f"✅ 생성 완료: {filename} ({DURATION:.1f}초)")


def generate_all_10_bgms(out_dir="assets/audio/bgm"):
    os.makedirs(out_dir, exist_ok=True)
    notes = get_frequencies()
    total_samples = int(DURATION * SAMPLE_RATE)
    
    print("🎵 한자 획순 쓰기 구간 클린 음소거 BGM 10곡 갱신 시작...\n")

    # =========================================================
    # 01. 햇살 마림바 & 톡톡 칼림바 (Marimba Sunshine)
    # =========================================================
    t1 = np.zeros(total_samples)
    melody_1 = [
        # [0s ~ 3.5s 인트로]
        ("C5", 0.5, 0.45), ("E5", 0.9, 0.48), ("G5", 1.3, 0.5), ("A5", 1.7, 0.48),
        ("G5", 2.2, 0.45), ("E5", 2.7, 0.42), ("C5", 3.1, 0.45),
        # [13.0s+ 아웃트로 축하 멜로디]
        ("C6", 13.0, 0.55), ("G5", 13.5, 0.45), ("E5", 14.5, 0.4), ("C5", 16.0, 0.38),
        ("G4", 18.0, 0.35), ("C5", 20.5, 0.38), ("C4", 23.5, 0.3)
    ]
    for n, tm, a in melody_1:
        if tm < DURATION:
            s_idx = int(tm * SAMPLE_RATE)
            m_s = synth_marimba(notes[n], 1.0, a)
            l = min(len(m_s), total_samples - s_idx)
            t1[s_idx:s_idx + l] += m_s[:l]
            if tm in [1.7, 13.0]:
                k_s = synth_crystal_bell(notes[n], 2.5, 0.4)
                lk = min(len(k_s), total_samples - s_idx)
                t1[s_idx:s_idx + lk] += k_s[:lk]
    save_wav(os.path.join(out_dir, "01_marimba_sunshine.wav"), t1)

    # =========================================================
    # 02. 동양풍 감성 로파이 에듀 (Lofi Oriental Study)
    # =========================================================
    t2 = np.zeros(total_samples)
    melody_2 = [
        ("G4", 0.5, 0.4), ("A4", 1.2, 0.42), ("C5", 1.9, 0.45), ("D5", 2.6, 0.48), ("E5", 3.1, 0.45),
        ("G5", 13.0, 0.55), ("E5", 14.2, 0.45), ("D5", 15.6, 0.42), ("C5", 17.0, 0.4), ("G4", 19.5, 0.35), ("C4", 23.0, 0.3)
    ]
    for n, tm, a in melody_2:
        if tm < DURATION:
            s_idx = int(tm * SAMPLE_RATE)
            g_s = synth_gayageum(notes[n], 2.2, a)
            l = min(len(g_s), total_samples - s_idx)
            t2[s_idx:s_idx + l] += g_s[:l]
            p_s = synth_piano(notes[n], 2.5, a * 0.45)
            lp = min(len(p_s), total_samples - s_idx)
            t2[s_idx:s_idx + lp] += p_s[:lp]
    save_wav(os.path.join(out_dir, "02_lofi_oriental_study.wav"), t2)

    # =========================================================
    # 03. 마법 숲 칼림바 & 요정 차임 (Kalimba Magic Forest)
    # =========================================================
    t3 = np.zeros(total_samples)
    melody_3 = [
        ("E5", 0.3, 0.45), ("G5", 0.8, 0.48), ("B5", 1.4, 0.5), ("E6", 2.0, 0.55), ("D6", 2.7, 0.48), ("B5", 3.2, 0.45),
        ("E6", 13.0, 0.58), ("B5", 14.0, 0.48), ("G5", 15.5, 0.42), ("E5", 17.5, 0.38), ("B4", 20.5, 0.32), ("E4", 24.0, 0.28)
    ]
    for n, tm, a in melody_3:
        if tm < DURATION:
            s_idx = int(tm * SAMPLE_RATE)
            k_s = synth_kalimba(notes[n], 1.8, a)
            l = min(len(k_s), total_samples - s_idx)
            t3[s_idx:s_idx + l] += k_s[:l]
            if tm in [2.0, 13.0]:
                c_s = synth_crystal_bell(notes[n], 2.5, 0.45)
                lc = min(len(c_s), total_samples - s_idx)
                t3[s_idx:s_idx + lc] += c_s[:lc]
    save_wav(os.path.join(out_dir, "03_kalimba_magic_forest.wav"), t3)

    # =========================================================
    # 04. 장난꾸러기 피치카토 바이올린 (Upbeat Pizzicato Play)
    # =========================================================
    t4 = np.zeros(total_samples)
    melody_4 = [
        ("C4", 0.25, 0.42), ("E4", 0.6, 0.45), ("G4", 1.0, 0.48), ("C5", 1.4, 0.52),
        ("B4", 1.8, 0.45), ("G4", 2.3, 0.42), ("C5", 2.8, 0.5), ("E5", 3.2, 0.52),
        ("C6", 13.0, 0.6), ("G5", 13.8, 0.48), ("E5", 15.0, 0.42), ("C5", 17.0, 0.38), ("G4", 20.0, 0.32), ("C4", 23.5, 0.28)
    ]
    for n, tm, a in melody_4:
        if tm < DURATION:
            s_idx = int(tm * SAMPLE_RATE)
            p_s = synth_pizzicato(notes[n], 0.8, a)
            l = min(len(p_s), total_samples - s_idx)
            t4[s_idx:s_idx + l] += p_s[:l]
    save_wav(os.path.join(out_dir, "04_upbeat_pizzicato_play.wav"), t4)

    # =========================================================
    # 05. 청아한 대숲 옹달샘 힐링 (Zen Bamboo Stream)
    # =========================================================
    t5 = np.zeros(total_samples)
    melody_5 = [
        ("D4", 0.5, 0.4), ("A4", 1.4, 0.45), ("D5", 2.2, 0.5), ("F5", 3.0, 0.48),
        ("D6", 13.0, 0.55), ("A5", 14.5, 0.45), ("F5", 16.5, 0.4), ("D5", 19.0, 0.35), ("A4", 22.0, 0.3)
    ]
    for n, tm, a in melody_5:
        if tm < DURATION:
            s_idx = int(tm * SAMPLE_RATE)
            p_s = synth_piano(notes[n], 3.0, a)
            l = min(len(p_s), total_samples - s_idx)
            t5[s_idx:s_idx + l] += p_s[:l]
    save_wav(os.path.join(out_dir, "05_zen_bamboo_stream.wav"), t5)

    # =========================================================
    # 06. 신나는 우쿨렐레 & 휘파람 바운스 (Happy Ukulele Bounce)
    # =========================================================
    t6 = np.zeros(total_samples)
    melody_6 = [
        ("C5", 0.3, 0.42), ("G4", 0.7, 0.4), ("C5", 1.2, 0.45), ("E5", 1.8, 0.5), ("G5", 2.4, 0.52), ("C6", 3.1, 0.55),
        ("C6", 13.0, 0.6), ("A5", 14.0, 0.5), ("G5", 15.2, 0.45), ("E5", 17.0, 0.4), ("C5", 19.5, 0.35), ("C4", 23.0, 0.3)
    ]
    for n, tm, a in melody_6:
        if tm < DURATION:
            s_idx = int(tm * SAMPLE_RATE)
            m_s = synth_marimba(notes[n], 0.8, a)
            l = min(len(m_s), total_samples - s_idx)
            t6[s_idx:s_idx + l] += m_s[:l]
    save_wav(os.path.join(out_dir, "06_happy_ukulele_bounce.wav"), t6)

    # =========================================================
    # 07. 트렌디 오리엔탈 퓨전 비트 (Asian Fusion Groove)
    # =========================================================
    t7 = np.zeros(total_samples)
    melody_7 = [
        ("A4", 0.3, 0.45), ("C5", 0.8, 0.48), ("D5", 1.4, 0.5), ("E5", 2.0, 0.52), ("G5", 2.6, 0.55), ("A5", 3.2, 0.58),
        ("A5", 13.0, 0.6), ("G5", 14.2, 0.5), ("E5", 15.8, 0.45), ("D5", 17.5, 0.4), ("A4", 21.0, 0.35)
    ]
    for n, tm, a in melody_7:
        if tm < DURATION:
            s_idx = int(tm * SAMPLE_RATE)
            g_s = synth_gayageum(notes[n], 1.5, a)
            l = min(len(g_s), total_samples - s_idx)
            t7[s_idx:s_idx + l] += g_s[:l]
    save_wav(os.path.join(out_dir, "07_asian_fusion_groove.wav"), t7)

    # =========================================================
    # 08. 스마트 한자 탐정 클랙 (Smart Detective Clack)
    # =========================================================
    t8 = np.zeros(total_samples)
    melody_8 = [
        ("C4", 0.3, 0.42), ("E4", 0.8, 0.45), ("G4", 1.4, 0.48), ("C5", 2.0, 0.52), ("G5", 2.7, 0.55), ("C6", 3.2, 0.6),
        ("C6", 13.0, 0.62), ("G5", 14.0, 0.52), ("E5", 15.5, 0.45), ("C5", 17.5, 0.4), ("C4", 22.0, 0.3)
    ]
    for n, tm, a in melody_8:
        if tm < DURATION:
            s_idx = int(tm * SAMPLE_RATE)
            m_s = synth_marimba(notes[n], 0.6, a)
            l = min(len(m_s), total_samples - s_idx)
            t8[s_idx:s_idx + l] += m_s[:l]
    save_wav(os.path.join(out_dir, "08_smart_detective_clack.wav"), t8)

    # =========================================================
    # 09. 달콤 오르골 & 별빛 벨 (Sweet Musicbox Lullaby)
    # =========================================================
    t9 = np.zeros(total_samples)
    melody_9 = [
        ("C5", 0.4, 0.45), ("E5", 1.0, 0.48), ("G5", 1.6, 0.5), ("C6", 2.3, 0.55), ("E6", 3.0, 0.58),
        ("C6", 13.0, 0.6), ("G5", 14.5, 0.48), ("E5", 16.5, 0.42), ("C5", 19.0, 0.38), ("C4", 23.0, 0.3)
    ]
    for n, tm, a in melody_9:
        if tm < DURATION:
            s_idx = int(tm * SAMPLE_RATE)
            mb_s = synth_musicbox(notes[n], 2.5, a)
            l = min(len(mb_s), total_samples - s_idx)
            t9[s_idx:s_idx + l] += mb_s[:l]
    save_wav(os.path.join(out_dir, "09_sweet_musicbox_lullaby.wav"), t9)

    # =========================================================
    # 10. 당당한 상형문자 어드벤처 (Epic Kid Adventure)
    # =========================================================
    t10 = np.zeros(total_samples)
    melody_10 = [
        ("C4", 0.3, 0.45), ("G4", 0.8, 0.5), ("C5", 1.3, 0.55), ("E5", 1.8, 0.58), ("G5", 2.4, 0.62), ("C6", 3.1, 0.68),
        ("C6", 13.0, 0.7), ("E6", 13.6, 0.72), ("C6", 14.4, 0.65), ("G5", 15.8, 0.55), ("E5", 17.5, 0.48), ("C5", 20.0, 0.4), ("C4", 24.0, 0.35)
    ]
    for n, tm, a in melody_10:
        if tm < DURATION:
            s_idx = int(tm * SAMPLE_RATE)
            m_s = synth_marimba(notes[n], 1.0, a)
            l = min(len(m_s), total_samples - s_idx)
            t10[s_idx:s_idx + l] += m_s[:l]
            b_s = synth_crystal_bell(notes[n], 2.2, a * 0.5)
            lb = min(len(b_s), total_samples - s_idx)
            t10[s_idx:s_idx + lb] += b_s[:lb]
    save_wav(os.path.join(out_dir, "10_epic_kid_adventure.wav"), t10)

    # 기본 활성 BGM(hanzi_study_bgm.wav)을 1위 트랙으로 동기화
    default_bgm = "assets/audio/hanzi_study_bgm.wav"
    save_wav(default_bgm, t1)
    print(f"\n🎉 10개 프리미엄 한자 학습 BGM 갱신 완료!")

if __name__ == "__main__":
    generate_all_10_bgms()
