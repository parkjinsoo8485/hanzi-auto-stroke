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

## 🚀 다른 컴퓨터에서 빠른 시작 (원클릭)
 
 ### 방법 1: `START.bat` 더블클릭 (가장 추천)
 1. GitHub에서 본 저장소를 `git clone` 합니다.
 2. 폴더 안에 있는 **`START.bat`** 파일을 더블클릭합니다.
 3. 시스템이 자동으로 **FFmpeg 설치 여부 / Python 가상환경 / 필수 라이브러리 / 160자 에셋**을 점검하고 **누락된 것이 있으면 전자동으로 설치**한 후 메뉴를 띄워줍니다.
 
 ### 방법 2: 수동 명령어로 실행
 ```powershell
 # 1. 환경 자동 세팅 스크립트 실행
 .\setup_environment.bat
 
 # 2. 원하는 한자 숏폼 렌더링
 .\.venv\Scripts\python.exe run_generator.py --char 車 --quality m
 ```

---

## 📂 파일 구조
- [src/short_scene.py](file:///c:/My_Project/Hnazi_auto_stroke/src/short_scene.py): Manim 세로 9:16 애니메이션 씬
- [src/pipeline.py](file:///c:/My_Project/Hnazi_auto_stroke/src/pipeline.py): 전체 자동화 파이프라인 및 FFmpeg 믹서
- [src/hanzi_data.py](file:///c:/My_Project/Hnazi_auto_stroke/src/hanzi_data.py): 상형문자 10종 데이터베이스
- [src/animcjk_loader.py](file:///c:/My_Project/Hnazi_auto_stroke/src/animcjk_loader.py): AnimCJK 획순 데이터 로더
- [PROCESS.md](file:///c:/My_Project/Hnazi_auto_stroke/PROCESS.md): 제작 과정 및 아키텍처 상세 문서
