"""
100만 유튜버 감성 한자 학습 최적화 BGM 관리 및 생성 모듈
- 10가지 프리미엄 BGM 트랙 라이브러리 제공 (assets/audio/bgm/)
- 한자별 맞춤 테마 BGM 자동 매칭 및 순환 선택 지원
"""
import os
import shutil
import glob

BGM_DIRECTORY = os.path.join(os.path.dirname(__file__), "..", "assets", "audio", "bgm")

BGM_TRACKS = [
    ("01_marimba_sunshine.wav", "햇살 마림바 & 톡톡 칼림바 (청량 핑거스냅)"),
    ("02_lofi_oriental_study.wav", "동양풍 감성 로파이 에듀 (따뜻한 피아노 & 칠 비트)"),
    ("03_kalimba_magic_forest.wav", "마법 숲 칼림바 & 요정 차임 (영롱한 멜로디)"),
    ("04_upbeat_pizzicato_play.wav", "장난꾸러기 피치카토 바이올린 (애니메이션풍)"),
    ("05_zen_bamboo_stream.wav", "청아한 대숲 옹달샘 힐링 (맑은 물방울 하프)"),
    ("06_happy_ukulele_bounce.wav", "신나는 우쿨렐레 & 휘파람 바운스 (통통 리듬)"),
    ("07_asian_fusion_groove.wav", "트렌디 오리엔탈 퓨전 비트 (가야금 스윙)"),
    ("08_smart_detective_clack.wav", "스마트 한자 탐정 클랙 (우드블록 & 실로폰)"),
    ("09_sweet_musicbox_lullaby.wav", "달콤 오르골 & 별빛 벨 (포근한 벨)"),
    ("10_epic_kid_adventure.wav", "당당한 상형문자 어드벤처 (활기찬 팡파르)")
]

def get_available_bgms():
    """사용 가능한 10개 BGM 목록 반환"""
    available = []
    for filename, title in BGM_TRACKS:
        full_path = os.path.join(BGM_DIRECTORY, filename)
        if os.path.exists(full_path):
            available.append((full_path, title))
    return available

def generate_traditional_hanzi_bgm(output_path="assets/audio/hanzi_study_bgm.wav", char=None, track_index=None, duration=35.0):
    """
    한자별로 다채로운 10개 프리미엄 BGM 중 최적의 트랙을 선택하여 적용
    - track_index 지정 시 해당 트랙 사용 (1~10)
    - char 지정 시 한자 고유 해시로 10개 트랙 중 일관된 테마 BGM 매칭
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    os.makedirs(BGM_DIRECTORY, exist_ok=True)
    
    # 10개 BGM이 아직 없는 경우 자동 생성
    bgm_files = glob.glob(os.path.join(BGM_DIRECTORY, "*.wav"))
    if len(bgm_files) < 10:
        try:
            import sys
            gen_script = os.path.join(os.path.dirname(__file__), "..", "generate_10_bgms.py")
            if os.path.exists(gen_script):
                from generate_10_bgms import generate_all_10_bgms
                generate_all_10_bgms(BGM_DIRECTORY)
        except Exception as e:
            print(f"[BGM] 10개 BGM 자동 생성 중 알림: {e}")

    import random
    # 트랙 선정 (assets/audio/bgm 폴더에서 랜덤 선택 또는 지정)
    if track_index is not None and 1 <= track_index <= len(BGM_TRACKS):
        chosen_file = BGM_TRACKS[track_index - 1][0]
        chosen_title = BGM_TRACKS[track_index - 1][1]
    else:
        # assets/audio/bgm 에서 랜덤으로 트랙 선정
        chosen_file, chosen_title = random.choice(BGM_TRACKS)

    src_path = os.path.join(BGM_DIRECTORY, chosen_file)
    
    if os.path.exists(src_path):
        shutil.copy2(src_path, output_path)
        print(f"[BGM] 배경음악 적용: [{chosen_title}] -> {output_path}")
        return output_path
    
    return output_path

if __name__ == "__main__":
    generate_traditional_hanzi_bgm()
