# 🎨 Sweet Hanzi Auto Shorts (상형문자 1인칭 서예 숏폼 자동 생성기)

> **그림 ➡️ 번체 한자 모핑 + 1인칭 POV 실사 손 붓글씨 + 정통 한국식 해서체 획순 + 듀얼 TTS 및 서예 SFX 숏폼 영상 생성 파이프라인**

---

## 🌟 주요 특징

1. **상형문자 픽토그램 모핑 (Visual Hook)**: 초반 3초간 상형문자 기원 그림이 한자로 자연스럽게 변신하여 시청 지속 시간 극대화.
2. **1인칭 POV 실사 손 붓글씨 모션**: 스튜디오 실사 손 에셋과 정밀 붓촉 오프셋 계산을 통해 실제 사람이 화선지에 글씨를 쓰는 듯한 연출.
3. **정통 한국식 해서체 획순 (AnimCJK)**: 한국식 번체/정자체 유니코드 기반의 정확한 획 분할 및 필순 가이드.
4. **한국어 & 미국 원어민 듀얼 TTS**: `ko-KR-SunHiNeural` + `en-US-JennyNeural` 성우 음성 및 아날로그 붓 마찰 효과음 자동 믹싱.
5. **원클릭 자동 렌더링**: 한자 입력 한 줄로 1080x1920 세로 숏폼 영상(mp4) 무한 양산.

---

## 🚀 빠른 시작

### 1. 가상환경 세팅 및 패키지 설치
```powershell
python -m venv .venv
.\.venv\Scripts\pip install manim edge-tts svgelements pygame pydub opencv-python Pillow
```

### 2. 숏폼 생성 실행
```powershell
# 「大」(큰 대) 숏폼 영상 렌더링
.\.venv\Scripts\python.exe run_generator.py --char 大 --quality m

# 「日」(날 일) 숏폼 영상 렌더링
.\.venv\Scripts\python.exe run_generator.py --char 日 --quality m

# 「木」(나무 목) 숏폼 영상 렌더링
.\.venv\Scripts\python.exe run_generator.py --char 木 --quality m
```

---

## 📂 파일 구조
- [src/short_scene.py](file:///c:/My_Project/Hnazi_auto_stroke/src/short_scene.py): Manim 세로 9:16 애니메이션 씬
- [src/pipeline.py](file:///c:/My_Project/Hnazi_auto_stroke/src/pipeline.py): 전체 자동화 파이프라인 및 FFmpeg 믹서
- [src/hanzi_data.py](file:///c:/My_Project/Hnazi_auto_stroke/src/hanzi_data.py): 상형문자 10종 데이터베이스
- [src/animcjk_loader.py](file:///c:/My_Project/Hnazi_auto_stroke/src/animcjk_loader.py): AnimCJK 획순 데이터 로더
- [PROCESS.md](file:///c:/My_Project/Hnazi_auto_stroke/PROCESS.md): 제작 과정 및 아키텍처 상세 문서
