# 📜 상형문자 1인칭 실사 손 붓글씨 숏폼 제작 과정 및 아키텍처 가이드 (PROCESS.md)

이 문서는 **"그림 ➡️ 한자 모핑(상형문자 진화) + 1인칭 POV 실사 손 붓글씨 + 한국식 정통 획순 + 듀얼 TTS 및 SFX"** 15초 교육용 숏폼 자동 생성 파이프라인의 전체 기획, 설계, 수학적 구현 및 최적화 과정을 상세히 기록한 제작 백서입니다.

---

## 📌 1. 프로젝트 기획 및 숏폼 훅(Hook) 설계

### 🎯 1.1. 제작 목적
- 초등/중등 한자 학습자 및 글로벌 한자 입문자를 위해 시청 지속 시간을 극대화하는 **15초 세로(9:16) 숏폼 템플릿** 구축.
- **세계적 벤치마킹:** [YouTube Shorts 참고 영상](https://youtube.com/shorts/-JHZZSJVCTE?si=zUP3U9plPWwjzvbd)의 1인칭 서예 연출 및 직관적인 시각적 모핑.

### ⏱️ 1.2. 15초 타임라인 구조
1. **[0.0s ~ 3.5s] 시각적 훅 (Visual Hook - 10초 만에 깨우치는 한자)**
   - 상단 타이틀 배너: **「10초 만에 깨우치는 한자」** 등장.
   - 상형문자의 기원이 되는 단순 픽토그램/일러스트 SVG 등장.
   - Manim의 `ReplacementTransform`을 통해 픽토그램의 선들이 이동하며 정통 해서체 한자로 부드럽게 변신.
   - 음성: 또렷하게 증폭된 볼륨(1.8x)으로 상형문자 설명 가이드 TTS 출력 (예: *"사람이 팔다리를 활짝 벌린 모양!"*).
2. **[3.5s ~ 11.0s] 1인칭 실사 손 붓글씨 획순 (POV Brush Stroke Writing)**
   - 전통 화선지 텍스처 배경과 연한 미산(米) 격자판 위에 실사 손과 붓(ImageMobject)이 착지(Landing).
   - 상단 헤더가 `부수 {char} | 총 N획`, `{char} {훈음}` 정보로 부드럽게 전환.
   - 한자별 고유 획순 명칭(가로, 세로, 삐침, 파임 등)에 맞춘 정확한 가이드 성우 음성 출력 (예: `日` - *"첫 번째, 왼쪽 세로긋기!"* ➡️ *"두 번째, 꺾어내리기!"*).
   - AnimCJK 정통 해서체 획순 궤적을 따라 붓촉이 이동하며 실시간으로 딥 코발트 블루 먹물이 채워지고 **실제 화선지 붓글씨 마찰 사운드(ASMR SFX)** 동시 출력.
3. **[11.0s ~ 14.0s] 훈음 카드 (Korean & English Dual TTS)**
   - 세련된 다크 글래스 카드 팝업: 한자 배지 + 한국어 훈음 (예: *"큰 대"*) + 영어 번역 (예: `[EN]` *"Big, Great"*).
   - 한국어 성우(`ko-KR-SunHiNeural`) 및 미국 고급 원어민 성우(`en-US-AriaNeural`) 순차 발음.
   - 슬래시(/) 발음 없이 자연스러운 쉼표 호흡으로 낭독.
4. **[14.0s ~ 18.5s] 실생활 활용 단어 (Real-life Vocabulary)**
   - 대표 활용 단어 카드 팝업 (예: `大人 (대인)` - *"마음이 넓고 훌륭한 사람 (Adult, Great person)"*).
   - 핵심 단어 발음 및 설명 TTS 출력 후 강조 애니메이션으로 마무리.

---

## 🛠️ 2. 기술 스택 및 디렉터리 아키텍처

### ⚙️ 2.1. 기술 스택
- **언어 및 런타임**: Python 3.12 (가상환경 `.venv`)
- **수학 애니메이션 엔진**: `Manim Community Edition (v0.21.0)`
- **음성 합성 (TTS)**: `edge-tts` (한국어 SunHiNeural, 미국 고급 영어 AriaNeural)
- **오디오 합성 & 비디오 믹싱**: `FFmpeg 8.1.1` (adelay, amix 멀티트랙 필터)
- **에셋 처리**: `OpenCV (cv2)`, `Pillow (PIL)`, `svgelements`
- **한자 획순 데이터**: `AnimCJK` (한국 번체/정자체 해서체 SVG `svgsKo`)

### 📂 2.2. 프로젝트 구조
```
Hnazi_auto_stroke/
├── assets/
│   ├── animcjk_cache/          # AnimCJK에서 다운로드된 한국식 한자 SVG 캐시
│   ├── audio/                  # 글자별 생성된 TTS 음성 및 실사 붓글씨 SFX 파일
│   ├── hand_brush_clean.png    # 투명 누끼 처리된 초고화질 실사 손+붓 에셋
│   ├── hanji_bg.png            # 전통 화선지 텍스처
│   ├── svg_drawings/           # 상형문자 원본 픽토그램 SVG
│   └── svg_hanzi/              # 획별 분할 및 윤곽선 SVG
├── src/
│   ├── animcjk_loader.py       # AnimCJK 획순 SVG 자동 다운로더 & 획 데이터 파서
│   ├── hanzi_data.py           # 상형문자 10종 메타데이터, 정확한 획 명칭 & SVG DB
│   ├── short_scene.py          # Manim 9:16 세로 숏폼 렌더링 씬
│   ├── tts_generator.py        # 한국어/원어민 영어 듀얼 TTS 비동기 생성기
│   ├── generate_sfx.py         # 서예 붓글씨 화선지 마찰 실사 효과음 관리자
│   └── pipeline.py             # 전체 프로세스 통합 원클릭 파이프라인 러너
├── output/                     # 최종 렌더링된 숏폼 비디오 (.mp4)
├── run_generator.py            # CLI 엔트리포인트 스크립트
├── PROCESS.md                  # 제작 과정 및 아키텍처 문서
└── README.md                   # 프로젝트 사용법 및 가이드
```

---

## 🔍 3. 주요 기술 구현 및 최적화 과정

### 📐 3.1. AnimCJK 한국 정통 해서체(정자체/번체) 획순 연동 & 획 명칭 정밀화
- 한국에서 통용되는 정통 획순(`svgsKo`) 유니코드 SVG를 실시간 호출.
- 각 한자의 획별 특성에 맞는 고유 획순 명칭(`stroke_names`)을 데이터베이스에 구축하여 획을 그을 때 정확한 획 명칭(가로, 세로, 삐침, 파임, 꺾음, 갈고리 등)을 성우가 읽도록 구현.

### ✍️ 3.2. 1인칭 POV 실사 손+붓 모션의 정밀 수학 보정 & 실사 서예 SFX
- 스튜디오 조명 기반 실사 손 에셋의 붓촉 끝점(DL) 오프셋 벡터 `tip_offset = np.array([width * 0.4876, height * 0.4881, 0.0])` 적용.
- 획의 중심선 좌표군 `manim_pts`에 `tip_offset`을 더한 궤적으로 `MoveAlongPath`를 실행하여 붓촉이 획선을 1:1로 일치하여 따라감.
- 실제 화선지 위 붓글씨 마찰 사운드를 샘플링하여 획이 그어질 때마다 실감 나는 서예 ASMR 연출.

### 🎙️ 3.3. 한국어 음량 증폭 및 고급 미국 영문 내레이션 (AriaNeural)
- 초반 훅 설명 음성이 작게 들리던 문제를 해결하기 위해 `edge-tts`의 `volume="+35%"` 옵션 및 FFmpeg 오디오 믹서의 `volume=1.8` 배율 적용.
- 영문 성우를 프리미엄 `en-US-AriaNeural`로 업그레이드하고 슬래시(/) 발음을 원천 차단하여 자연스럽고 세련된 영어 학습 음성 제공.

---

## 🚀 4. 실행 방법

```powershell
# 「大」(큰 대) 숏폼 영상 렌더링
.\.venv\Scripts\python.exe run_generator.py --char 大 --quality m

# 「日」(날 일) 숏폼 영상 렌더링
.\.venv\Scripts\python.exe run_generator.py --char 日 --quality m
```
