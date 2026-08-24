"""
1000만 숏폼 감성 한자 학습 최적화 BGM 생성 모듈
- [0s ~ 3.8s 훅 인트로]: 시선을 확 사로잡는 영롱한 크리스탈 차임(Ting! ✨) & 주목 멜로디
- [3.8s ~ 13.5s 붓글씨 라이팅 (대폭 개선)]:
  * 아이들과 성인 모두에게 중독성 있고 기분 좋은 청량한 마림바(Marimba) & 칼림바(Kalimba) & 피치카토(Pizzicato) 멜로디
  * 무거운 둔탁한 킥 대신 산뜻하고 경쾌한 핑거스냅 & 에그 쉐이커 리듬
- [13.5s ~ 25s 훈음/단어]: 글자 완성 축하 쉬머링 차임 + 교육 내레이션 가청성을 위한 맑고 따뜻한 어쿠스틱 여운
"""
import os
import wave
import numpy as np

def generate_traditional_hanzi_bgm(output_path="assets/audio/hanzi_study_bgm.wav", duration=25.0, sample_rate=44100):
    """아이와 어른 모두 좋아하는 통통 튀고 청량한 1000만 숏폼 한자 학습 BGM 생성"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    total_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, total_samples, endpoint=False)
    
    # 맑고 경쾌한 C Major / A Minor 밝은 펜타토닉 음계 주파수 테이블
    notes_freq = {
        "C3": 130.81, "E3": 164.81, "G3": 196.00, "A3": 220.00,
        "C4": 261.63, "D4": 293.66, "E4": 329.63, "G4": 392.00, "A4": 440.00,
        "C5": 523.25, "D5": 587.33, "E5": 659.25, "G5": 783.99, "A5": 880.00,
        "C6": 1046.50, "D6": 1174.66, "E6": 1318.51, "G6": 1567.98
    }
    
    # ==========================================
    # 1. 인트로 영롱한 크리스탈 차임 (0s & 13.0s 글자 완성)
    # ==========================================
    bell_audio = np.zeros(total_samples)
    bell_events = [(0.05, 1.0), (12.8, 0.9)]
    
    for hit_t, b_vol in bell_events:
        if hit_t >= duration:
            continue
        start_idx = int(hit_t * sample_rate)
        bell_len = int(4.0 * sample_rate)
        hit_samples = min(bell_len, total_samples - start_idx)
        bt = np.linspace(0, 4.0, hit_samples, endpoint=False)
        
        # 영롱한 글래스 하모닉스
        partials = [(1046.50, 1.0, 3.2), (1567.98, 0.65, 2.6), (2093.00, 0.40, 2.0), (2637.02, 0.25, 1.5)]
        tone = np.zeros(hit_samples)
        for freq, amp, dec in partials:
            tone += amp * np.sin(2 * np.pi * freq * bt) * np.exp(-bt * (3.0 / dec))
        shimmer = 1.0 + 0.12 * np.sin(2 * np.pi * 5.5 * bt)
        bell_audio[start_idx:start_idx + hit_samples] += tone * shimmer * 0.32 * b_vol

    # ==========================================
    # 2. [가운데 핵심] 아이/어른 모두 좋아하는 통통 튀는 마림바 & 칼림바 & 피치카토
    # ==========================================
    marimba_audio = np.zeros(total_samples)
    
    # 통통 튀는 경쾌한 멜로디 시퀀스 [(시간, 음계, 강도, 마림바/칼림바 타입)]
    marimba_events = [
        # [0s ~ 3.8s 훅 인트로 파트]: 호기심 유발 귀여운 멜로디
        (0.25, "C5", 0.35, "bell"),
        (0.65, "E5", 0.38, "marimba"),
        (1.05, "G5", 0.42, "marimba"),
        (1.45, "A5", 0.40, "bell"),
        (2.00, "G5", 0.36, "marimba"),
        (2.50, "E5", 0.38, "marimba"),
        (3.00, "C5", 0.40, "bell"),
        
        # [3.8s ~ 13.0s 붓글씨 파트]: 경쾌하고 기분 좋은 도파민 마림바 & 칼림바 핑퐁 리듬
        (3.85, "G4", 0.32, "marimba"),
        (4.25, "C5", 0.36, "kalimba"),
        (4.65, "E5", 0.38, "marimba"),
        (5.05, "G5", 0.42, "kalimba"),
        (5.50, "E5", 0.34, "marimba"),
        (5.90, "D5", 0.32, "kalimba"),
        (6.30, "C5", 0.36, "marimba"),
        (6.70, "A4", 0.32, "kalimba"),
        (7.15, "C5", 0.36, "marimba"),
        (7.55, "E5", 0.38, "kalimba"),
        (7.95, "G5", 0.42, "marimba"),
        (8.40, "A5", 0.40, "kalimba"),
        (8.80, "G5", 0.36, "marimba"),
        (9.20, "E5", 0.34, "kalimba"),
        (9.65, "D5", 0.35, "marimba"),
        (10.05, "C5", 0.38, "kalimba"),
        (10.50, "E5", 0.38, "marimba"),
        (10.90, "G5", 0.42, "kalimba"),
        (11.35, "A5", 0.40, "marimba"),
        (11.80, "C6", 0.45, "bell"),
        (12.30, "G5", 0.38, "kalimba"),
        
        # [13.0s ~ 25s 훈음/단어 파트]: 부드럽고 따뜻한 어쿠스틱 여운
        (13.2, "E5", 0.28, "kalimba"),
        (14.5, "C5", 0.25, "bell"),
        (16.5, "G4", 0.22, "kalimba"),
        (19.0, "C5", 0.25, "bell"),
        (22.0, "C4", 0.20, "bell")
    ]

    for start_t, note_name, amp, inst_type in marimba_events:
        if start_t >= duration:
            continue
        freq = notes_freq.get(note_name, 440.0)
        start_idx = int(start_t * sample_rate)
        
        if inst_type == "marimba":
            # 따뜻하고 둥근 우드 마림바 톤 (빠른 우드 어택 + 부드러운 감쇠)
            note_dur = 0.8
            n_samples = min(int(note_dur * sample_rate), total_samples - start_idx)
            nt = np.linspace(0, note_dur, n_samples, endpoint=False)
            
            env = np.exp(-nt * 8.5) * (1.0 - np.exp(-nt * 300.0))
            # 마림바 배음: 기본파 + 4배음(우드 바 공명) + 가벼운 클릭
            body = (
                1.00 * np.sin(2 * np.pi * freq * nt) +
                0.35 * np.sin(2 * np.pi * (freq * 4.0) * nt) * np.exp(-nt * 22.0) +
                0.12 * np.sin(2 * np.pi * (freq * 10.0) * nt) * np.exp(-nt * 60.0)
            )
            click = np.random.uniform(-0.15, 0.15, n_samples) * np.exp(-nt * 250.0)
            marimba_audio[start_idx:start_idx + n_samples] += (body + click) * env * amp

        elif inst_type == "kalimba":
            # 맑고 찰랑이는 칼림바/오르골 톤 (반짝이는 금속 튕김)
            note_dur = 1.2
            n_samples = min(int(note_dur * sample_rate), total_samples - start_idx)
            nt = np.linspace(0, note_dur, n_samples, endpoint=False)
            
            env = np.exp(-nt * 4.5) * (1.0 - np.exp(-nt * 200.0))
            tine = (
                1.00 * np.sin(2 * np.pi * freq * nt) +
                0.45 * np.sin(2 * np.pi * (freq * 2.98) * nt) * np.exp(-nt * 8.0) +
                0.20 * np.sin(2 * np.pi * (freq * 5.92) * nt) * np.exp(-nt * 15.0)
            )
            ping = np.random.uniform(-0.08, 0.08, n_samples) * np.exp(-nt * 180.0)
            marimba_audio[start_idx:start_idx + n_samples] += (tine + ping) * env * amp

        else:  # bell
            note_dur = 1.8
            n_samples = min(int(note_dur * sample_rate), total_samples - start_idx)
            nt = np.linspace(0, note_dur, n_samples, endpoint=False)
            env = np.exp(-nt * 2.8) * (1.0 - np.exp(-nt * 150.0))
            tone = (
                1.00 * np.sin(2 * np.pi * freq * nt) +
                0.30 * np.sin(2 * np.pi * (freq * 2.0) * nt) * np.exp(-nt * 4.0)
            )
            marimba_audio[start_idx:start_idx + n_samples] += tone * env * amp

    # ==========================================
    # 3. [산뜻한 퍼커션] 핑거스냅 & 에그 쉐이커 (무거운 킥 완전 제거)
    # ==========================================
    perc_audio = np.zeros(total_samples)
    step_time = 0.22  # 약 136 BPM 경쾌한 템포
    
    # 0.5초부터 13.2초까지 경쾌하게 가동
    p_t = 0.5
    step_idx = 0
    while p_t < min(duration, 13.2):
        s_idx = int(p_t * sample_rate)
        
        # 1) 에그 쉐이커 (치키치키 상쾌한 리듬: 매 스텝마다)
        shaker_len = int(0.08 * sample_rate)
        sh_samples = min(shaker_len, total_samples - s_idx)
        st = np.linspace(0, 0.08, sh_samples, endpoint=False)
        shaker_env = np.exp(-st * 50.0) * (0.8 + 0.4 * (step_idx % 2))
        shaker_noise = np.random.uniform(-0.15, 0.15, sh_samples) * shaker_env
        perc_audio[s_idx:s_idx + sh_samples] += shaker_noise * 0.25

        # 2) 산뜻한 핑거스냅 / 림클릭 (짝! 짝! 기분 좋은 박수 2박/4박)
        if step_idx % 4 == 2:
            snap_len = int(0.12 * sample_rate)
            sn_samples = min(snap_len, total_samples - s_idx)
            snt = np.linspace(0, 0.12, sn_samples, endpoint=False)
            snap_env = np.exp(-snt * 45.0)
            snap_body = np.sin(2 * np.pi * 950.0 * snt) * np.exp(-snt * 60.0)
            snap_click = np.random.uniform(-0.25, 0.25, sn_samples) * np.exp(-snt * 80.0)
            perc_audio[s_idx:s_idx + sn_samples] += (snap_body * 0.4 + snap_click * 0.6) * snap_env * 0.32

        p_t += step_time
        step_idx += 1

    # ==========================================
    # 4. 부드러운 화음 패드 (Warm Acoustic Harmony)
    # ==========================================
    pad_audio = np.zeros(total_samples)
    chord_freqs = [130.81, 196.00, 261.63, 329.63]  # C3, G3, C4, E4
    for cf in chord_freqs:
        lfo = 0.5 + 0.5 * np.sin(2 * np.pi * 0.12 * t + cf)
        pad_audio += 0.035 * np.sin(2 * np.pi * cf * t) * lfo

    # ==========================================
    # 5. 전체 믹싱 & 마스터링
    # ==========================================
    mixed = bell_audio + marimba_audio + perc_audio + pad_audio
    
    # 페이드 인 (0.2초) / 페이드 아웃 (2.0초)
    fade_in_len = int(0.2 * sample_rate)
    fade_out_len = int(2.0 * sample_rate)
    mixed[:fade_in_len] *= np.linspace(0, 1, fade_in_len)
    mixed[-fade_out_len:] *= np.linspace(1, 0, fade_out_len)
    
    # 노멀라이즈 (-1.0dB)
    max_val = np.max(np.abs(mixed))
    if max_val > 0:
        mixed = mixed / max_val * 0.88
        
    audio_int16 = (mixed * 32767).astype(np.int16)
    
    with wave.open(output_path, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_int16.tobytes())
        
    print(f"[BGM] 1000만 숏폼 감성 청량 마림바&칼림바 BGM 생성 완료: {output_path} ({duration:.1f}초)")
    return output_path

if __name__ == "__main__":
    generate_traditional_hanzi_bgm()
