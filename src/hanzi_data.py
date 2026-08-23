"""
상형문자 및 한국식 한자(번체) 메타데이터 & SVG 패스 정의 데이터베이스
- 교육적 가치가 높은 대표 상형문자 10종 완벽 구성
- 한국식 번체/정자체 획순 및 획별 정확한 명칭(가로, 세로, 삐침, 파임 등), 훈음, 영문 번역, 실생활 활용 단어 수록
- 슬래시(/) 없이 자연스러운 영문 표기 적용
"""

HANZI_DATABASE = {
    "大": {
        "char": "大",
        "stroke_count": 3,
        "hun_eum": "큰 대",
        "hun_eum_en": "Big, Great",
        "sound_desc": "사람이 팔다리를 활짝 벌린 모양",
        "example_word": "大人 (대인)",
        "example_word_desc": "마음이 넓고 훌륭한 사람 (Adult, Great person)",
        "stroke_names": [
            "첫 번째, 가로긋기!",
            "두 번째, 왼쪽 삐침!",
            "세 번째, 오른쪽 파임!"
        ],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <circle cx="512" cy="200" r="70" fill="#FFD166" stroke="#EF476F" stroke-width="24" stroke-linecap="round"/>
  <path d="M 160 480 Q 512 440 864 480" fill="none" stroke="#EF476F" stroke-width="48" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 512 280 L 512 500 Q 420 720 220 900" fill="none" stroke="#EF476F" stroke-width="48" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 512 500 Q 604 720 804 900" fill="none" stroke="#EF476F" stroke-width="48" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""
    },
    "日": {
        "char": "日",
        "stroke_count": 4,
        "hun_eum": "날 일",
        "hun_eum_en": "Day, Sun",
        "sound_desc": "둥근 해(태양)와 가운데 흑점 모양",
        "example_word": "日曜日 (일요일)",
        "example_word_desc": "태양의 날, 한 주의 첫날 (Sunday)",
        "stroke_names": [
            "첫 번째, 왼쪽 세로긋기!",
            "두 번째, 꺾어내리기!",
            "세 번째, 가운데 가로긋기!",
            "네 번째, 아래 가로 닫기!"
        ],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <circle cx="512" cy="512" r="260" fill="#FFB703" stroke="#FB8500" stroke-width="36"/>
  <circle cx="512" cy="512" r="50" fill="#FB8500"/>
  <line x1="512" y1="120" x2="512" y2="200" stroke="#FB8500" stroke-width="36" stroke-linecap="round"/>
  <line x1="512" y1="824" x2="512" y2="904" stroke="#FB8500" stroke-width="36" stroke-linecap="round"/>
  <line x1="120" y1="512" x2="200" y2="512" stroke="#FB8500" stroke-width="36" stroke-linecap="round"/>
  <line x1="824" y1="512" x2="904" y2="512" stroke="#FB8500" stroke-width="36" stroke-linecap="round"/>
</svg>"""
    },
    "木": {
        "char": "木",
        "stroke_count": 4,
        "hun_eum": "나무 목",
        "hun_eum_en": "Tree, Wood",
        "sound_desc": "줄기와 가지, 뿌리가 뻗은 나무 모양",
        "example_word": "木曜日 (목요일)",
        "example_word_desc": "나무의 기운을 담은 날 (Thursday)",
        "stroke_names": [
            "첫 번째, 가로긋기!",
            "두 번째, 가운데 세로긋기!",
            "세 번째, 왼쪽 삐침!",
            "네 번째, 오른쪽 파임!"
        ],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <path d="M 512 180 L 512 850" fill="none" stroke="#2D6A4F" stroke-width="48" stroke-linecap="round"/>
  <path d="M 220 480 Q 512 430 804 480" fill="none" stroke="#2D6A4F" stroke-width="44" stroke-linecap="round"/>
  <path d="M 512 480 Q 360 660 200 840" fill="none" stroke="#2D6A4F" stroke-width="44" stroke-linecap="round"/>
  <path d="M 512 480 Q 664 660 824 840" fill="none" stroke="#2D6A4F" stroke-width="44" stroke-linecap="round"/>
  <circle cx="512" cy="220" r="80" fill="#52B788" opacity="0.6"/>
  <circle cx="320" cy="460" r="70" fill="#52B788" opacity="0.6"/>
  <circle cx="704" cy="460" r="70" fill="#52B788" opacity="0.6"/>
</svg>"""
    },
    "山": {
        "char": "山",
        "stroke_count": 3,
        "hun_eum": "뫼 산",
        "hun_eum_en": "Mountain",
        "sound_desc": "세 개의 봉우리가 우뚝 솟은 산 모양",
        "example_word": "登山 (등산)",
        "example_word_desc": "산에 올라 자연을 즐김 (Climbing mountain)",
        "stroke_names": [
            "첫 번째, 가운데 세로긋기!",
            "두 번째, 꺾어올리기!",
            "세 번째, 오른쪽 세로긋기!"
        ],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <path d="M 200 800 L 320 420 L 440 680 L 512 240 L 584 680 L 704 420 L 824 800 Z" fill="#606C38" stroke="#283618" stroke-width="32" stroke-linejoin="round"/>
</svg>"""
    },
    "水": {
        "char": "水",
        "stroke_count": 4,
        "hun_eum": "물 수",
        "hun_eum_en": "Water",
        "sound_desc": "굽이쳐 흐르는 물줄기와 물방울 모양",
        "example_word": "水曜日 (수요일)",
        "example_word_desc": "물의 날, 한 주의 가운데 날 (Wednesday)",
        "stroke_names": [
            "첫 번째, 가운데 갈고리!",
            "두 번째, 왼쪽 가로 꺾음!",
            "세 번째, 왼쪽 삐침!",
            "네 번째, 오른쪽 파임!"
        ],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <path d="M 512 180 Q 460 512 512 850" fill="none" stroke="#0077B6" stroke-width="52" stroke-linecap="round"/>
  <path d="M 240 380 Q 340 440 380 560" fill="none" stroke="#0096C7" stroke-width="38" stroke-linecap="round"/>
  <path d="M 220 740 L 380 620" fill="none" stroke="#0096C7" stroke-width="38" stroke-linecap="round"/>
  <path d="M 780 400 L 640 540" fill="none" stroke="#0096C7" stroke-width="38" stroke-linecap="round"/>
  <path d="M 640 560 Q 740 700 840 760" fill="none" stroke="#0096C7" stroke-width="38" stroke-linecap="round"/>
</svg>"""
    },
    "月": {
        "char": "月",
        "stroke_count": 4,
        "hun_eum": "달 월",
        "hun_eum_en": "Moon, Month",
        "sound_desc": "밤하늘에 떠 있는 초승달 모양",
        "example_word": "月曜日 (월요일)",
        "example_word_desc": "달의 기운이 깃든 한 주의 시작 (Monday)",
        "stroke_names": [
            "첫 번째, 왼쪽 삐침!",
            "두 번째, 꺾어 갈고리!",
            "세 번째, 안쪽 가로긋기!",
            "네 번째, 아래 가로 닫기!"
        ],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <path d="M 620 200 A 340 340 0 1 0 620 824 A 260 260 0 0 1 620 200 Z" fill="#F4D06F" stroke="#E29578" stroke-width="24"/>
</svg>"""
    },
    "火": {
        "char": "火",
        "stroke_count": 4,
        "hun_eum": "불 화",
        "hun_eum_en": "Fire, Flame",
        "sound_desc": "이글거리며 타오르는 불꽃 모양",
        "example_word": "火曜日 (화요일)",
        "example_word_desc": "불의 날, 활기찬 화요일 (Tuesday)",
        "stroke_names": [
            "첫 번째, 왼쪽 점찍기!",
            "두 번째, 오른쪽 점찍기!",
            "세 번째, 가운데 삐침!",
            "네 번째, 오른쪽 파임!"
        ],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <path d="M 512 180 Q 640 400 512 650 Q 380 400 512 180 Z" fill="#E63946"/>
  <path d="M 320 480 Q 380 620 240 780" fill="none" stroke="#F4A261" stroke-width="42" stroke-linecap="round"/>
  <path d="M 704 480 Q 640 620 784 780" fill="none" stroke="#F4A261" stroke-width="42" stroke-linecap="round"/>
  <path d="M 512 480 Q 420 700 280 860" fill="none" stroke="#E63946" stroke-width="48" stroke-linecap="round"/>
  <path d="M 512 480 Q 604 700 744 860" fill="none" stroke="#E63946" stroke-width="48" stroke-linecap="round"/>
</svg>"""
    },
    "人": {
        "char": "人",
        "stroke_count": 2,
        "hun_eum": "사람 인",
        "hun_eum_en": "Person, Human",
        "sound_desc": "두 사람이 서로 기대어 서 있는 모양",
        "example_word": "人間 (인간)",
        "example_word_desc": "사람과 사람이 더불어 살아가는 존재 (Human)",
        "stroke_names": [
            "첫 번째, 왼쪽 삐침!",
            "두 번째, 오른쪽 파임!"
        ],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <circle cx="512" cy="220" r="90" fill="#FFD166" stroke="#E76F51" stroke-width="24"/>
  <path d="M 512 320 Q 420 580 240 860" fill="none" stroke="#E76F51" stroke-width="48" stroke-linecap="round"/>
  <path d="M 440 540 Q 580 680 780 860" fill="none" stroke="#E76F51" stroke-width="48" stroke-linecap="round"/>
</svg>"""
    },
    "門": {
        "char": "門",
        "stroke_count": 8,
        "hun_eum": "문 문",
        "hun_eum_en": "Door, Gate",
        "sound_desc": "좌우로 열리는 대문의 두 짝 모양",
        "example_word": "校門 (교문)",
        "example_word_desc": "학교로 들어가는 정문 (School gate)",
        "stroke_names": [
            "첫 번째, 왼쪽 세로긋기!",
            "두 번째, 꺾어내리기!",
            "세 번째, 가로긋기!",
            "네 번째, 가로 닫기!",
            "다섯 번째, 오른쪽 점찍기!",
            "여섯 번째, 꺾어 갈고리!",
            "일곱 번째, 가로긋기!",
            "여덟 번째, 가로 닫기!"
        ],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="220" y="240" width="240" height="600" fill="#E9ECEF" stroke="#495057" stroke-width="32" rx="10"/>
  <rect x="564" y="240" width="240" height="600" fill="#E9ECEF" stroke="#495057" stroke-width="32" rx="10"/>
  <circle cx="420" cy="540" r="24" fill="#F59E0B"/>
  <circle cx="604" cy="540" r="24" fill="#F59E0B"/>
</svg>"""
    },
    "川": {
        "char": "川",
        "stroke_count": 3,
        "hun_eum": "내 천",
        "hun_eum_en": "River, Stream",
        "sound_desc": "세 줄기의 냇물이 나란히 흘러가는 모양",
        "example_word": "河川 (하천)",
        "example_word_desc": "자연적으로 흐르는 크고 작은 물줄기 (River)",
        "stroke_names": [
            "첫 번째, 왼쪽 삐침!",
            "두 번째, 가운데 세로긋기!",
            "세 번째, 오른쪽 세로긋기!"
        ],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <path d="M 280 200 Q 240 512 280 824" fill="none" stroke="#00B4D8" stroke-width="48" stroke-linecap="round"/>
  <path d="M 512 260 Q 512 512 512 760" fill="none" stroke="#0077B6" stroke-width="48" stroke-linecap="round"/>
  <path d="M 744 200 Q 784 512 744 824" fill="none" stroke="#00B4D8" stroke-width="48" stroke-linecap="round"/>
</svg>"""
    }
}
