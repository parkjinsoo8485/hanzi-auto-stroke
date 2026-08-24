"""
상형문자 및 한국식 한자(번체/정자체) 160자 마스터 메타데이터 & SVG 데이터베이스
- 총 고유 등록 상형한자: 160자 (중복 없음)
- AnimCJK 한국 한자(정자체) 획순, 훈음, 영문 번역, 상형 유래, 실생활 단어 완벽 수록
"""

HANZI_DATABASE = {
    "日": {
        "char": "日",
        "stroke_count": 4,
        "hun_eum": "날 일",
        "hun_eum_en": "Day, Sun",
        "sound_desc": "둥근 해와 가운데 흑점 모양",
        "example_word": "日曜日 (일요일)",
        "example_word_desc": "태양의 날, 한 주의 첫날 (Sunday)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">日</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "月": {
        "char": "月",
        "stroke_count": 4,
        "hun_eum": "달 월",
        "hun_eum_en": "Moon, Month",
        "sound_desc": "밤하늘에 떠 있는 초승달 모양",
        "example_word": "月曜日 (월요일)",
        "example_word_desc": "달의 기운이 깃든 월요일 (Monday)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">月</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "山": {
        "char": "山",
        "stroke_count": 3,
        "hun_eum": "뫼 산",
        "hun_eum_en": "Mountain",
        "sound_desc": "세 개의 봉우리가 우뚝 솟은 산 모양",
        "example_word": "登山 (등산)",
        "example_word_desc": "산에 오름 (Climbing mountain)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">山</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "水": {
        "char": "水",
        "stroke_count": 4,
        "hun_eum": "물 수",
        "hun_eum_en": "Water",
        "sound_desc": "굽이쳐 흐르는 물줄기와 물방울 모양",
        "example_word": "水曜日 (수요일)",
        "example_word_desc": "물의 날, 수요일 (Wednesday)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">水</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "火": {
        "char": "火",
        "stroke_count": 4,
        "hun_eum": "불 화",
        "hun_eum_en": "Fire, Flame",
        "sound_desc": "이글거리며 타오르는 불꽃 모양",
        "example_word": "火曜日 (화요일)",
        "example_word_desc": "불의 날, 화요일 (Tuesday)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">火</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "川": {
        "char": "川",
        "stroke_count": 3,
        "hun_eum": "내 천",
        "hun_eum_en": "River, Stream",
        "sound_desc": "세 줄기의 냇물이 나란히 흘러가는 모양",
        "example_word": "河川 (하천)",
        "example_word_desc": "자연적으로 흐르는 물줄기 (River)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">川</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "雨": {
        "char": "雨",
        "stroke_count": 8,
        "hun_eum": "비 우",
        "hun_eum_en": "Rain",
        "sound_desc": "하늘 구름에서 빗방울이 떨어지는 모양",
        "example_word": "雨傘 (우산)",
        "example_word_desc": "비를 가리는 우산 (Umbrella)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">雨</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "土": {
        "char": "土",
        "stroke_count": 3,
        "hun_eum": "흙 토",
        "hun_eum_en": "Earth, Soil",
        "sound_desc": "땅 위로 흙덩이가 솟아난 모양",
        "example_word": "土地 (토지)",
        "example_word_desc": "사람이 이용하는 땅 (Land)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">土</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "石": {
        "char": "石",
        "stroke_count": 5,
        "hun_eum": "돌 석",
        "hun_eum_en": "Stone, Rock",
        "sound_desc": "언덕 아래에 굴러떨어진 돌 모양",
        "example_word": "石造 (석조)",
        "example_word_desc": "돌로 만든 구조물 (Stone structure)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">石</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "風": {
        "char": "風",
        "stroke_count": 9,
        "hun_eum": "바람 풍",
        "hun_eum_en": "Wind",
        "sound_desc": "공기가 소용돌이치며 부는 바람 모양",
        "example_word": "風景 (풍경)",
        "example_word_desc": "자연의 아름다운 경치 (Scenery)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">風</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "雲": {
        "char": "雲",
        "stroke_count": 12,
        "hun_eum": "구름 운",
        "hun_eum_en": "Cloud",
        "sound_desc": "하늘에 뭉게뭉게 피어오르는 구름 모양",
        "example_word": "雲海 (운해)",
        "example_word_desc": "바다처럼 넓게 펼쳐진 구름 (Sea of clouds)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">雲</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "泉": {
        "char": "泉",
        "stroke_count": 9,
        "hun_eum": "샘 천",
        "hun_eum_en": "Spring, Fountain",
        "sound_desc": "바위틈에서 맑은 물이 솟아나는 샘 모양",
        "example_word": "溫泉 (온천)",
        "example_word_desc": "지하에서 솟는 따뜻한 샘물 (Hot spring)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">泉</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "谷": {
        "char": "谷",
        "stroke_count": 7,
        "hun_eum": "골 곡",
        "hun_eum_en": "Valley, Canyon",
        "sound_desc": "산과 산 사이에 깊게 파인 골짜기 모양",
        "example_word": "溪谷 (계곡)",
        "example_word_desc": "산골짜기에 흐르는 맑은 물 (Valley)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">谷</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "原": {
        "char": "原",
        "stroke_count": 10,
        "hun_eum": "언덕 원",
        "hun_eum_en": "Field, Origin",
        "sound_desc": "언덕 아래 샘물이 솟아나는 들판 모양",
        "example_word": "高原 (고원)",
        "example_word_desc": "해발 고도가 높은 들판 (Plateau)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">原</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "氣": {
        "char": "氣",
        "stroke_count": 10,
        "hun_eum": "기운 기",
        "hun_eum_en": "Energy, Steam",
        "sound_desc": "구름과 따뜻한 김이 피어오르는 기운 모양",
        "example_word": "空氣 (공기)",
        "example_word_desc": "지구를 둘러싼 숨 쉬는 기운 (Air)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">氣</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "大": {
        "char": "大",
        "stroke_count": 3,
        "hun_eum": "큰 대",
        "hun_eum_en": "Big, Great",
        "sound_desc": "사람이 팔다리를 활짝 벌린 모양",
        "example_word": "大人 (대인)",
        "example_word_desc": "마음이 넓고 훌륭한 사람 (Great person)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">大</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "人": {
        "char": "人",
        "stroke_count": 2,
        "hun_eum": "사람 인",
        "hun_eum_en": "Person, Human",
        "sound_desc": "두 사람이 서로 기대어 서 있는 모양",
        "example_word": "人間 (인간)",
        "example_word_desc": "더불어 살아가는 사람 (Human)",
        "stroke_names": ["1번째 획!", "2번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">人</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "女": {
        "char": "女",
        "stroke_count": 3,
        "hun_eum": "여자 녀",
        "hun_eum_en": "Woman, Female",
        "sound_desc": "얌전하게 무릎 꿇고 앉은 여인의 모양",
        "example_word": "女性 (여성)",
        "example_word_desc": "여자의 성별 (Female)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">女</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "子": {
        "char": "子",
        "stroke_count": 3,
        "hun_eum": "아들 자",
        "hun_eum_en": "Child, Son",
        "sound_desc": "머리가 크고 포대에 싸인 아기의 모양",
        "example_word": "子孫 (자손)",
        "example_word_desc": "대대로 이어지는 후손 (Descendant)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">子</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "目": {
        "char": "目",
        "stroke_count": 5,
        "hun_eum": "눈 목",
        "hun_eum_en": "Eye, Vision",
        "sound_desc": "눈동자와 눈꺼풀의 윤곽 모양",
        "example_word": "注目 (주목)",
        "example_word_desc": "관심을 가지고 바라봄 (Attention)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">目</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "耳": {
        "char": "耳",
        "stroke_count": 6,
        "hun_eum": "귀 이",
        "hun_eum_en": "Ear, Hearing",
        "sound_desc": "소리를 듣는 귓바퀴와 귓구멍 모양",
        "example_word": "耳目 (이목)",
        "example_word_desc": "귀와 눈, 세상 사람들의 관심 (Attention)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">耳</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "口": {
        "char": "口",
        "stroke_count": 3,
        "hun_eum": "입 구",
        "hun_eum_en": "Mouth, Opening",
        "sound_desc": "말하고 밥을 먹는 사람의 입 모양",
        "example_word": "入口 (입구)",
        "example_word_desc": "안으로 들어가는 문 (Entrance)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">口</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "手": {
        "char": "手",
        "stroke_count": 4,
        "hun_eum": "손 수",
        "hun_eum_en": "Hand",
        "sound_desc": "다섯 손가락을 활짝 편 손 모양",
        "example_word": "手紙 (편지)",
        "example_word_desc": "손으로 정성껏 쓴 편지 (Letter)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">手</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "足": {
        "char": "足",
        "stroke_count": 7,
        "hun_eum": "발 족",
        "hun_eum_en": "Foot, Leg",
        "sound_desc": "종아리와 발바닥의 모양",
        "example_word": "遠足 (원족)",
        "example_word_desc": "소풍이나 야외 나들이 (Picnic)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">足</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "心": {
        "char": "心",
        "stroke_count": 4,
        "hun_eum": "마음 심",
        "hun_eum_en": "Heart, Mind",
        "sound_desc": "피가 통하는 심장의 모양",
        "example_word": "心臟 (심장)",
        "example_word_desc": "가슴속에서 뛰는 심장 (Heart)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">心</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "首": {
        "char": "首",
        "stroke_count": 9,
        "hun_eum": "머리 수",
        "hun_eum_en": "Head, Neck",
        "sound_desc": "머리카락과 눈이 달린 머리 모양",
        "example_word": "首都 (수도)",
        "example_word_desc": "나라의 으뜸가는 도시 (Capital)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">首</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "頭": {
        "char": "頭",
        "stroke_count": 16,
        "hun_eum": "머리 두",
        "hun_eum_en": "Head",
        "sound_desc": "사람의 얼굴과 두개골 모양",
        "example_word": "頭腦 (두뇌)",
        "example_word_desc": "생각하고 판단하는 뇌 (Brain)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">頭</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "面": {
        "char": "面",
        "stroke_count": 9,
        "hun_eum": "얼굴 면",
        "hun_eum_en": "Face, Surface",
        "sound_desc": "이마와 뺨이 있는 사람의 얼굴 모양",
        "example_word": "面談 (면담)",
        "example_word_desc": "서로 얼굴을 맞대고 이야기함 (Interview)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">面</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "齒": {
        "char": "齒",
        "stroke_count": 15,
        "hun_eum": "이 치",
        "hun_eum_en": "Tooth, Teeth",
        "sound_desc": "입안에 가지런히 솟은 치아 모양",
        "example_word": "齒科 (치과)",
        "example_word_desc": "이를 치료하는 병원 (Dentistry)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">齒</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "舌": {
        "char": "舌",
        "stroke_count": 6,
        "hun_eum": "혀 설",
        "hun_eum_en": "Tongue",
        "sound_desc": "입 밖으로 날름 내민 혀 모양",
        "example_word": "舌戰 (설전)",
        "example_word_desc": "말과 논리로 다투는 싸움 (War of words)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">舌</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鼻": {
        "char": "鼻",
        "stroke_count": 14,
        "hun_eum": "코 비",
        "hun_eum_en": "Nose",
        "sound_desc": "숨을 쉬는 코의 모양",
        "example_word": "鼻音 (비음)",
        "example_word_desc": "코를 울려서 내는 소리 (Nasal sound)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鼻</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "身": {
        "char": "身",
        "stroke_count": 7,
        "hun_eum": "몸 신",
        "hun_eum_en": "Body, Person",
        "sound_desc": "아이를 밴 사람의 몸 모양",
        "example_word": "身體 (신체)",
        "example_word_desc": "사람의 육체 (Body)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">身</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "骨": {
        "char": "骨",
        "stroke_count": 10,
        "hun_eum": "뼈 골",
        "hun_eum_en": "Bone, Skeleton",
        "sound_desc": "살을 발라낸 뼈대의 마디 모양",
        "example_word": "骨格 (골격)",
        "example_word_desc": "몸의 뼈대 구조 (Skeleton)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">骨</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "肉": {
        "char": "肉",
        "stroke_count": 6,
        "hun_eum": "고기 육",
        "hun_eum_en": "Meat, Flesh",
        "sound_desc": "결이 있는 붉은 고기 덩어리 모양",
        "example_word": "筋肉 (근육)",
        "example_word_desc": "몸을 움직이는 살과 근육 (Muscle)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">肉</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "血": {
        "char": "血",
        "stroke_count": 6,
        "hun_eum": "피 혈",
        "hun_eum_en": "Blood",
        "sound_desc": "제사 그릇에 담긴 붉은 피 모양",
        "example_word": "血管 (혈관)",
        "example_word_desc": "피가 흐르는 혈관 (Blood vessel)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">血</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "毛": {
        "char": "毛",
        "stroke_count": 4,
        "hun_eum": "털 모",
        "hun_eum_en": "Hair, Fur",
        "sound_desc": "부드럽게 자라난 털의 모양",
        "example_word": "毛髮 (모발)",
        "example_word_desc": "사람의 머리털 (Hair)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">毛</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "皮": {
        "char": "皮",
        "stroke_count": 5,
        "hun_eum": "가죽 피",
        "hun_eum_en": "Skin, Leather",
        "sound_desc": "짐승의 털을 벗겨낸 생가죽 모양",
        "example_word": "皮膚 (피부)",
        "example_word_desc": "몸을 덮고 있는 살갗 (Skin)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">皮</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "爪": {
        "char": "爪",
        "stroke_count": 4,
        "hun_eum": "손톱 조",
        "hun_eum_en": "Claw, Nail",
        "sound_desc": "손가락 끝에 달린 날카로운 손톱 모양",
        "example_word": "爪甲 (조갑)",
        "example_word_desc": "손톱과 발톱 (Fingernail)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">爪</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "角": {
        "char": "角",
        "stroke_count": 7,
        "hun_eum": "뿔 각",
        "hun_eum_en": "Horn, Angle",
        "sound_desc": "짐승의 머리에 돋은 뾰족한 뿔 모양",
        "example_word": "角度 (각도)",
        "example_word_desc": "두 선이 이루는 모서리 각도 (Angle)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">角</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "母": {
        "char": "母",
        "stroke_count": 5,
        "hun_eum": "어머니 모",
        "hun_eum_en": "Mother",
        "sound_desc": "아이에게 젖을 먹이는 어머니의 모양",
        "example_word": "母情 (모정)",
        "example_word_desc": "어머니의 깊은 사랑 (Motherly love)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">母</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "父": {
        "char": "父",
        "stroke_count": 4,
        "hun_eum": "아버지 부",
        "hun_eum_en": "Father",
        "sound_desc": "손에 도끼나 회초리를 든 아버지 모양",
        "example_word": "父母 (부모)",
        "example_word_desc": "아버지와 어머니 (Parents)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">父</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "老": {
        "char": "老",
        "stroke_count": 6,
        "hun_eum": "늙을 로",
        "hun_eum_en": "Old, Elder",
        "sound_desc": "지팡이를 짚고 허리가 굽은 노인 모양",
        "example_word": "敬老 (경로)",
        "example_word_desc": "어르신을 공경함 (Respect for elderly)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">老</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "臣": {
        "char": "臣",
        "stroke_count": 6,
        "hun_eum": "신하 신",
        "hun_eum_en": "Servant, Subject",
        "sound_desc": "임금 앞에서 눈을 내리깐 신하의 눈 모양",
        "example_word": "忠臣 (충신)",
        "example_word_desc": "나라에 충성하는 신하 (Loyal subject)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">臣</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "牛": {
        "char": "牛",
        "stroke_count": 4,
        "hun_eum": "소 우",
        "hun_eum_en": "Cow, Ox",
        "sound_desc": "두 뿔이 위로 솟은 황소의 얼굴 모양",
        "example_word": "牛肉 (우육)",
        "example_word_desc": "맛있는 소고기 (Beef)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">牛</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "馬": {
        "char": "馬",
        "stroke_count": 10,
        "hun_eum": "말 마",
        "hun_eum_en": "Horse",
        "sound_desc": "갈기와 네 다리, 꼬리를 가진 말의 모양",
        "example_word": "競馬 (경마)",
        "example_word_desc": "말을 타고 달리는 경기 (Horse racing)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">馬</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "羊": {
        "char": "羊",
        "stroke_count": 6,
        "hun_eum": "양 양",
        "hun_eum_en": "Sheep, Goat",
        "sound_desc": "둥글게 말린 두 뿔을 가진 양의 머리 모양",
        "example_word": "羊毛 (양모)",
        "example_word_desc": "따뜻한 양의 털 (Wool)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">羊</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "豕": {
        "char": "豕",
        "stroke_count": 7,
        "hun_eum": "돼지 시",
        "hun_eum_en": "Pig, Boar",
        "sound_desc": "뚱뚱한 몸과 짧은 꼬리를 가진 돼지 모양",
        "example_word": "豕心 (시심)",
        "example_word_desc": "돼지처럼 욕심 많은 마음 (Greed)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">豕</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "犬": {
        "char": "犬",
        "stroke_count": 4,
        "hun_eum": "개 견",
        "hun_eum_en": "Dog, Canine",
        "sound_desc": "꼬리를 치켜올리고 짖는 개의 모양",
        "example_word": "忠犬 (충견)",
        "example_word_desc": "주인에게 충성스러운 개 (Faithful dog)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">犬</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鳥": {
        "char": "鳥",
        "stroke_count": 11,
        "hun_eum": "새 조",
        "hun_eum_en": "Bird",
        "sound_desc": "부리와 날개, 깃털을 가진 큰 새의 모양",
        "example_word": "白鳥 (백조)",
        "example_word_desc": "우아하고 하얀 백조 (Swan)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鳥</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "隹": {
        "char": "隹",
        "stroke_count": 8,
        "hun_eum": "새 추",
        "hun_eum_en": "Short-tailed Bird",
        "sound_desc": "꼬리가 짧고 통통한 작은 새의 모양",
        "example_word": "隹部 (추부)",
        "example_word_desc": "새와 관련된 한자 부수 (Bird radical)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">隹</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "魚": {
        "char": "魚",
        "stroke_count": 11,
        "hun_eum": "물고기 어",
        "hun_eum_en": "Fish",
        "sound_desc": "아가미와 비늘, 지느러미를 가진 물고기 모양",
        "example_word": "漁村 (어촌)",
        "example_word_desc": "바닷가 물고기 잡는 마을 (Fishing village)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">魚</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "蟲": {
        "char": "蟲",
        "stroke_count": 18,
        "hun_eum": "벌레 충",
        "hun_eum_en": "Insect, Bug",
        "sound_desc": "꿈틀거리는 세 마리의 벌레 모양",
        "example_word": "昆蟲 (곤충)",
        "example_word_desc": "작은 곤충과 벌레 (Insect)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!", "17번째 획!", "18번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">蟲</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "龜": {
        "char": "龜",
        "stroke_count": 16,
        "hun_eum": "거북 귀",
        "hun_eum_en": "Turtle, Tortoise",
        "sound_desc": "단단한 등껍질과 네 발을 가진 거북이 모양",
        "example_word": "龜甲 (귀갑)",
        "example_word_desc": "거북의 등껍질 (Turtle shell)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">龜</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "象": {
        "char": "象",
        "stroke_count": 12,
        "hun_eum": "코끼리 상",
        "hun_eum_en": "Elephant, Image",
        "sound_desc": "긴 코와 큰 귀, 굵은 다리를 가진 코끼리 모양",
        "example_word": "象牙 (상아)",
        "example_word_desc": "코끼리의 긴 어금니 (Ivory)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">象</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鹿": {
        "char": "鹿",
        "stroke_count": 11,
        "hun_eum": "사슴 록",
        "hun_eum_en": "Deer",
        "sound_desc": "아름다운 가지 뿔을 가진 사슴 모양",
        "example_word": "鹿茸 (녹용)",
        "example_word_desc": "사슴의 귀한 뿔 (Deer antler)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鹿</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "虎": {
        "char": "虎",
        "stroke_count": 8,
        "hun_eum": "호랑이 호",
        "hun_eum_en": "Tiger",
        "sound_desc": "줄무늬와 날카로운 발톱을 가진 호랑이 모양",
        "example_word": "虎穴 (호혈)",
        "example_word_desc": "호랑이의 깊은 굴 (Tiger den)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">虎</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "蛇": {
        "char": "蛇",
        "stroke_count": 11,
        "hun_eum": "뱀 사",
        "hun_eum_en": "Snake, Serpent",
        "sound_desc": "구불구불 기어가는 뱀의 모양",
        "example_word": "蛇足 (사족)",
        "example_word_desc": "뱀을 그리고 발을 덧붙인 군더더기 (Useless addition)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">蛇</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "龍": {
        "char": "龍",
        "stroke_count": 16,
        "hun_eum": "용 룡",
        "hun_eum_en": "Dragon",
        "sound_desc": "비늘과 뿔을 가진 신비로운 용의 모양",
        "example_word": "龍宮 (용궁)",
        "example_word_desc": "바닷속 용왕의 궁궐 (Dragon palace)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">龍</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "羽": {
        "char": "羽",
        "stroke_count": 6,
        "hun_eum": "깃 우",
        "hun_eum_en": "Feather, Wing",
        "sound_desc": "새의 양 날개에 돋은 깃털 모양",
        "example_word": "羽毛 (우모)",
        "example_word_desc": "새의 부드러운 깃털 (Feather)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">羽</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "尾": {
        "char": "尾",
        "stroke_count": 7,
        "hun_eum": "꼬리 미",
        "hun_eum_en": "Tail",
        "sound_desc": "짐승의 엉덩이에 달린 긴 꼬리 모양",
        "example_word": "語尾 (어미)",
        "example_word_desc": "말이나 문장의 맨 끝부분 (Word ending)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">尾</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "兔": {
        "char": "兔",
        "stroke_count": 8,
        "hun_eum": "토끼 토",
        "hun_eum_en": "Rabbit, Hare",
        "sound_desc": "긴 귀와 웅크린 몸을 가진 토끼 모양",
        "example_word": "兔角 (토각)",
        "example_word_desc": "토끼의 뿔처럼 세상에 없는 것 (Impossibility)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">兔</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鼠": {
        "char": "鼠",
        "stroke_count": 13,
        "hun_eum": "쥐 서",
        "hun_eum_en": "Mouse, Rat",
        "sound_desc": "수염과 앞니를 가진 쥐의 모양",
        "example_word": "鼠賊 (서적)",
        "example_word_desc": "쥐처럼 몰래 훔치는 도둑 (Sneak thief)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鼠</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "豚": {
        "char": "豚",
        "stroke_count": 11,
        "hun_eum": "돼지 돈",
        "hun_eum_en": "Pig, Pork",
        "sound_desc": "살이 통통하게 오른 아기 돼지 모양",
        "example_word": "豚肉 (돈육)",
        "example_word_desc": "맛있는 돼지고기 (Pork)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">豚</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "豸": {
        "char": "豸",
        "stroke_count": 7,
        "hun_eum": "벌레 치",
        "hun_eum_en": "Beast, Worm",
        "sound_desc": "몸을 구부려 먹이를 노리는 맹수 모양",
        "example_word": "豸部 (치부)",
        "example_word_desc": "맹수 한자 부수 (Beast radical)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">豸</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "燕": {
        "char": "燕",
        "stroke_count": 16,
        "hun_eum": "제비 연",
        "hun_eum_en": "Swallow",
        "sound_desc": "갈라진 꼬리 날개를 가진 제비 모양",
        "example_word": "燕尾 (연미)",
        "example_word_desc": "제비의 갈라진 꼬리 (Swallow tail)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">燕</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "貝": {
        "char": "貝",
        "stroke_count": 7,
        "hun_eum": "조개 패",
        "hun_eum_en": "Shell, Money",
        "sound_desc": "껍데기가 양쪽으로 벌어지는 조개 모양",
        "example_word": "貝類 (패류)",
        "example_word_desc": "조개와 굴 같은 조개류 (Shellfish)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">貝</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "蛙": {
        "char": "蛙",
        "stroke_count": 12,
        "hun_eum": "개구리 와",
        "hun_eum_en": "Frog",
        "sound_desc": "물가에서 폴짝 뛰는 개구리 모양",
        "example_word": "井蛙 (정와)",
        "example_word_desc": "우물 안 개구리 (Narrow-minded person)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">蛙</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鶴": {
        "char": "鶴",
        "stroke_count": 21,
        "hun_eum": "학 학",
        "hun_eum_en": "Crane",
        "sound_desc": "다리와 목이 긴 우아한 두루미 모양",
        "example_word": "鶴立 (학립)",
        "example_word_desc": "학처럼 홀로 우뚝 섬 (Standing out)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!", "17번째 획!", "18번째 획!", "19번째 획!", "20번째 획!", "21번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鶴</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鵝": {
        "char": "鵝",
        "stroke_count": 18,
        "hun_eum": "거위 아",
        "hun_eum_en": "Goose",
        "sound_desc": "물 위를 헤엄치는 거위 모양",
        "example_word": "鵝鳥 (아조)",
        "example_word_desc": "길들여 기르는 거위 (Domestic goose)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!", "17번째 획!", "18번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鵝</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鷹": {
        "char": "鷹",
        "stroke_count": 24,
        "hun_eum": "매 응",
        "hun_eum_en": "Hawk, Falcon",
        "sound_desc": "날카로운 눈빛과 부리를 가진 매의 모양",
        "example_word": "鷹眼 (응안)",
        "example_word_desc": "매처럼 날카로운 눈 (Sharp eyes)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!", "17번째 획!", "18번째 획!", "19번째 획!", "20번째 획!", "21번째 획!", "22번째 획!", "23번째 획!", "24번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鷹</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "蜂": {
        "char": "蜂",
        "stroke_count": 13,
        "hun_eum": "벌 봉",
        "hun_eum_en": "Bee, Wasp",
        "sound_desc": "침을 쏘며 날아다니는 꿀벌 모양",
        "example_word": "養蜂 (양봉)",
        "example_word_desc": "꿀을 얻기 위해 벌을 기름 (Beekeeping)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">蜂</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "蝶": {
        "char": "蝶",
        "stroke_count": 15,
        "hun_eum": "나비 접",
        "hun_eum_en": "Butterfly",
        "sound_desc": "넓은 날개로 펄펄 나는 나비 모양",
        "example_word": "胡蝶 (호접)",
        "example_word_desc": "아름답게 나는 나비 (Butterfly)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">蝶</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "蛛": {
        "char": "蛛",
        "stroke_count": 12,
        "hun_eum": "거미 주",
        "hun_eum_en": "Spider",
        "sound_desc": "줄을 치고 먹이를 잡는 거미 모양",
        "example_word": "蜘蛛 (지주)",
        "example_word_desc": "거미줄을 치는 거미 (Spider)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">蛛</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "蟻": {
        "char": "蟻",
        "stroke_count": 19,
        "hun_eum": "개미 의",
        "hun_eum_en": "Ant",
        "sound_desc": "부지런히 줄지어 일하는 개미 모양",
        "example_word": "蟻穴 (의혈)",
        "example_word_desc": "개미들이 사는 작은 굴 (Ant hill)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!", "17번째 획!", "18번째 획!", "19번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">蟻</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "熊": {
        "char": "熊",
        "stroke_count": 14,
        "hun_eum": "곰 웅",
        "hun_eum_en": "Bear",
        "sound_desc": "두 발로 일어서는 늠름한 곰 모양",
        "example_word": "熊膽 (웅담)",
        "example_word_desc": "곰의 귀한 쓸개 (Bear gallbladder)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">熊</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "木": {
        "char": "木",
        "stroke_count": 4,
        "hun_eum": "나무 목",
        "hun_eum_en": "Tree, Wood",
        "sound_desc": "줄기와 가지, 뿌리가 뻗은 나무 모양",
        "example_word": "木曜日 (목요일)",
        "example_word_desc": "나무의 기운이 깃든 목요일 (Thursday)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">木</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "艸": {
        "char": "艸",
        "stroke_count": 6,
        "hun_eum": "풀 초",
        "hun_eum_en": "Grass, Herb",
        "sound_desc": "땅에서 싹터 오른 두 줄기의 풀 모양",
        "example_word": "艸部 (초부)",
        "example_word_desc": "풀과 식물 관련 부수 (Grass radical)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">艸</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "竹": {
        "char": "竹",
        "stroke_count": 6,
        "hun_eum": "대나무 죽",
        "hun_eum_en": "Bamboo",
        "sound_desc": "마디마디 곧게 뻗은 대나무 잎 모양",
        "example_word": "竹林 (죽림)",
        "example_word_desc": "대나무가 울창한 숲 (Bamboo grove)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">竹</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "禾": {
        "char": "禾",
        "stroke_count": 5,
        "hun_eum": "벼 화",
        "hun_eum_en": "Grain, Rice plant",
        "sound_desc": "이삭이 탐스럽게 고개 숙인 벼 모양",
        "example_word": "禾穀 (화곡)",
        "example_word_desc": "벼와 보리 같은 모든 곡식 (Grains)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">禾</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "米": {
        "char": "米",
        "stroke_count": 6,
        "hun_eum": "쌀 미",
        "hun_eum_en": "Rice, Meter",
        "sound_desc": "탈곡하여 흩어진 낟알 쌀 모양",
        "example_word": "米穀 (미곡)",
        "example_word_desc": "도정한 하얀 쌀 (Milled rice)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">米</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "果": {
        "char": "果",
        "stroke_count": 8,
        "hun_eum": "열매 과",
        "hun_eum_en": "Fruit, Result",
        "sound_desc": "나무 위에 맺힌 둥근 열매 모양",
        "example_word": "果實 (과실)",
        "example_word_desc": "달콤하고 싱싱한 과일 (Fruit)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">果</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "瓜": {
        "char": "瓜",
        "stroke_count": 5,
        "hun_eum": "오이 과",
        "hun_eum_en": "Melon, Gourd",
        "sound_desc": "덩굴에 주렁주렁 매달린 오이 모양",
        "example_word": "瓜分 (과분)",
        "example_word_desc": "오이를 자르듯 나눔 (Division)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">瓜</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "桑": {
        "char": "桑",
        "stroke_count": 10,
        "hun_eum": "뽕나무 상",
        "hun_eum_en": "Mulberry",
        "sound_desc": "누에가 잎을 먹는 뽕나무 모양",
        "example_word": "桑田 (상전)",
        "example_word_desc": "뽕나무가 자라는 밭 (Mulberry field)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">桑</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "麥": {
        "char": "麥",
        "stroke_count": 11,
        "hun_eum": "보리 맥",
        "hun_eum_en": "Barley, Wheat",
        "sound_desc": "수염이 길게 자란 보리 이삭 모양",
        "example_word": "麥酒 (맥주)",
        "example_word_desc": "보리로 빚은 시원한 맥주 (Beer)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">麥</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "麻": {
        "char": "麻",
        "stroke_count": 11,
        "hun_eum": "삼 마",
        "hun_eum_en": "Hemp",
        "sound_desc": "집 안에서 껍질을 벗겨 말리는 삼베 삼 모양",
        "example_word": "麻布 (마포)",
        "example_word_desc": "삼으로 짠 시원한 베옷 (Hemp cloth)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">麻</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "豆": {
        "char": "豆",
        "stroke_count": 7,
        "hun_eum": "콩 두",
        "hun_eum_en": "Bean, Vessel",
        "sound_desc": "제사 그릇 모양에서 콩의 뜻으로 쓰인 모양",
        "example_word": "豆腐 (두부)",
        "example_word_desc": "콩으로 만든 부드러운 두부 (Tofu)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">豆</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "黍": {
        "char": "黍",
        "stroke_count": 12,
        "hun_eum": "기장 서",
        "hun_eum_en": "Millet",
        "sound_desc": "수확하여 묶어 놓은 기장 곡식 모양",
        "example_word": "黍粟 (서속)",
        "example_word_desc": "기장과 조 같은 곡식 (Millets)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">黍</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "林": {
        "char": "林",
        "stroke_count": 8,
        "hun_eum": "수풀 림",
        "hun_eum_en": "Forest, Grove",
        "sound_desc": "두 그루의 나무가 어우러진 숲 모양",
        "example_word": "森林 (삼림)",
        "example_word_desc": "나무가 무성한 큰 숲 (Forest)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">林</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "森": {
        "char": "森",
        "stroke_count": 12,
        "hun_eum": "수풀 삼",
        "hun_eum_en": "Dense Forest",
        "sound_desc": "세 그루의 나무가 빽빽하게 우거진 숲 모양",
        "example_word": "森嚴 (삼엄)",
        "example_word_desc": "숲처럼 빈틈없이 엄숙함 (Strict)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">森</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "根": {
        "char": "根",
        "stroke_count": 10,
        "hun_eum": "뿌리 근",
        "hun_eum_en": "Root, Base",
        "sound_desc": "나무가 땅속에 내린 단단한 뿌리 모양",
        "example_word": "根本 (근본)",
        "example_word_desc": "사물의 가장 밑바탕 뿌리 (Root cause)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">根</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "枝": {
        "char": "枝",
        "stroke_count": 8,
        "hun_eum": "가지 지",
        "hun_eum_en": "Branch, Twig",
        "sound_desc": "줄기에서 사방으로 뻗어나간 나뭇가지 모양",
        "example_word": "枝葉 (지엽)",
        "example_word_desc": "나뭇가지와 잎사귀 (Branch and leaf)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">枝</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "葉": {
        "char": "葉",
        "stroke_count": 12,
        "hun_eum": "잎 엽",
        "hun_eum_en": "Leaf, Foliage",
        "sound_desc": "가지 끝에 돋아난 넓은 잎사귀 모양",
        "example_word": "紅葉 (홍엽)",
        "example_word_desc": "가을에 붉게 물든 단풍잎 (Autumn leaves)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">葉</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "花": {
        "char": "花",
        "stroke_count": 8,
        "hun_eum": "꽃 화",
        "hun_eum_en": "Flower, Blossom",
        "sound_desc": "풀잎 위에 화려하게 피어난 꽃 모양",
        "example_word": "花園 (화원)",
        "example_word_desc": "꽃이 가득 핀 아름다운 뜰 (Flower garden)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">花</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "芽": {
        "char": "芽",
        "stroke_count": 8,
        "hun_eum": "싹 아",
        "hun_eum_en": "Sprout, Bud",
        "sound_desc": "봄날 땅을 뚫고 솟아오른 새싹 모양",
        "example_word": "發芽 (발아)",
        "example_word_desc": "씨앗에서 싹이 트임 (Germination)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">芽</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "苗": {
        "char": "苗",
        "stroke_count": 9,
        "hun_eum": "모 묘",
        "hun_eum_en": "Sprout, Seedling",
        "sound_desc": "논밭에 가지런히 심은 어린 볏모 모양",
        "example_word": "育苗 (육묘)",
        "example_word_desc": "어린 모를 정성껏 기름 (Raising seedlings)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">苗</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "田": {
        "char": "田",
        "stroke_count": 5,
        "hun_eum": "밭 전",
        "hun_eum_en": "Field, Farm",
        "sound_desc": "바둑판처럼 구획을 나눈 논밭 모양",
        "example_word": "水田 (수전)",
        "example_word_desc": "물이 가득 찬 벼농사 논 (Rice paddy)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">田</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "井": {
        "char": "井",
        "stroke_count": 4,
        "hun_eum": "우물 정",
        "hun_eum_en": "Well",
        "sound_desc": "우물가에 나무틀을 '우물 정'자로 짠 모양",
        "example_word": "井水 (정수)",
        "example_word_desc": "우물에서 길어 올린 맑은 물 (Well water)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">井</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "圃": {
        "char": "圃",
        "stroke_count": 10,
        "hun_eum": "채소밭 포",
        "hun_eum_en": "Garden, Nursery",
        "sound_desc": "울타리를 두르고 채소를 가꾸는 텃밭 모양",
        "example_word": "農圃 (농포)",
        "example_word_desc": "농사짓는 밭과 채소밭 (Farm field)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">圃</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "禾/穀": {
        "char": "禾/穀",
        "stroke_count": 14,
        "hun_eum": "곡식 곡",
        "hun_eum_en": "Grain, Cereal",
        "sound_desc": "곡식 껍질을 벗겨 찧는 모양",
        "example_word": "穀物 (곡물)",
        "example_word_desc": "사람이 먹는 모든 곡식 (Cereal grains)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">禾/穀</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "車": {
        "char": "車",
        "stroke_count": 7,
        "hun_eum": "수레 차",
        "hun_eum_en": "Cart, Car",
        "sound_desc": "두 바퀴와 짐칸을 갖춘 수레 모양",
        "example_word": "車道 (차도)",
        "example_word_desc": "자동차가 다니는 길 (Roadway)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">車</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "舟": {
        "char": "舟",
        "stroke_count": 6,
        "hun_eum": "배 주",
        "hun_eum_en": "Boat, Ship",
        "sound_desc": "물 위에 띄운 통나무 나룻배 모양",
        "example_word": "舟航 (주항)",
        "example_word_desc": "배를 타고 바다를 항해함 (Navigation)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">舟</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "刀": {
        "char": "刀",
        "stroke_count": 2,
        "hun_eum": "칼 도",
        "hun_eum_en": "Knife, Sword",
        "sound_desc": "손잡이와 날이 선 칼 모양",
        "example_word": "名刀 (명도)",
        "example_word_desc": "뛰어난 장인이 만든 명검 (Masterpiece sword)",
        "stroke_names": ["1번째 획!", "2번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">刀</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "弓": {
        "char": "弓",
        "stroke_count": 3,
        "hun_eum": "활 궁",
        "hun_eum_en": "Bow, Archery",
        "sound_desc": "시위를 팽팽하게 당긴 활 모양",
        "example_word": "弓道 (궁도)",
        "example_word_desc": "활을 쏘는 전통 무예 (Archery)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">弓</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "矢": {
        "char": "矢",
        "stroke_count": 5,
        "hun_eum": "화살 시",
        "hun_eum_en": "Arrow",
        "sound_desc": "화살촉과 깃이 달린 곧은 화살 모양",
        "example_word": "弓矢 (궁시)",
        "example_word_desc": "활과 화살 (Bow and arrow)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">矢</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "戈": {
        "char": "戈",
        "stroke_count": 4,
        "hun_eum": "창 과",
        "hun_eum_en": "Spear, Halberd",
        "sound_desc": "자루 끝에 꺾인 날이 달린 꺾창 모양",
        "example_word": "干戈 (간과)",
        "example_word_desc": "방패와 창, 곧 전쟁 (Shield and spear)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">戈</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "矛": {
        "char": "矛",
        "stroke_count": 5,
        "hun_eum": "창 모",
        "hun_eum_en": "Spear, Pike",
        "sound_desc": "뾰족한 칼날이 달린 긴 찌르는 창 모양",
        "example_word": "矛盾 (모순)",
        "example_word_desc": "창과 방패, 앞뒤가 맞지 않음 (Contradiction)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">矛</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "斤": {
        "char": "斤",
        "stroke_count": 4,
        "hun_eum": "도끼 근",
        "hun_eum_en": "Axe, Weight",
        "sound_desc": "나무를 찍는 날카로운 손도끼 모양",
        "example_word": "斤量 (근량)",
        "example_word_desc": "무게를 재는 단위 (Weight)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">斤</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "斧": {
        "char": "斧",
        "stroke_count": 8,
        "hun_eum": "도끼 부",
        "hun_eum_en": "Axe, Hatchet",
        "sound_desc": "장작을 패는 무거운 큰 도끼 모양",
        "example_word": "斧鉞 (부월)",
        "example_word_desc": "형벌을 내리는 도끼 (Battle axe)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">斧</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "網": {
        "char": "網",
        "stroke_count": 14,
        "hun_eum": "그물 망",
        "hun_eum_en": "Net, Network",
        "sound_desc": "물고기나 새를 잡는 얽힌 그물 모양",
        "example_word": "通信網 (통신망)",
        "example_word_desc": "서로 연결된 정보 통신 네트워크 (Network)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">網</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鼎": {
        "char": "鼎",
        "stroke_count": 13,
        "hun_eum": "솥 정",
        "hun_eum_en": "Cauldron, Tripod",
        "sound_desc": "세 다리와 두 귀가 달린 웅장한 솥 모양",
        "example_word": "鼎立 (정립)",
        "example_word_desc": "세 세력이 솥발처럼 맞섬 (Tripartite standoff)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鼎</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鬲": {
        "char": "鬲",
        "stroke_count": 10,
        "hun_eum": "솥 력",
        "hun_eum_en": "Cauldron, Pot",
        "sound_desc": "음식을 끓이는 속이 빈 세 다리 솥 모양",
        "example_word": "鬲部 (력부)",
        "example_word_desc": "옛 솥 관련 부수 (Cauldron radical)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鬲</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "皿": {
        "char": "皿",
        "stroke_count": 5,
        "hun_eum": "그릇 명",
        "hun_eum_en": "Dish, Plate",
        "sound_desc": "음식을 담는 오목한 접시 그릇 모양",
        "example_word": "食器 (식기)",
        "example_word_desc": "음식을 담는 그릇 (Tableware)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">皿</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "壺": {
        "char": "壺",
        "stroke_count": 12,
        "hun_eum": "병 호",
        "hun_eum_en": "Vessel, Pot",
        "sound_desc": "뚜껑과 둥근 몸통을 가진 단지 모양",
        "example_word": "壺中 (호중)",
        "example_word_desc": "항아리 속의 별천지 (Inside the jar)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">壺</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "缶": {
        "char": "缶",
        "stroke_count": 6,
        "hun_eum": "장군 부",
        "hun_eum_en": "Jar, Can",
        "sound_desc": "흙으로 빚은 둥근 장군 술병 모양",
        "example_word": "缶詰 (통조림)",
        "example_word_desc": "음식을 보관하는 캔 (Canned food)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">缶</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "臼": {
        "char": "臼",
        "stroke_count": 6,
        "hun_eum": "절구 구",
        "hun_eum_en": "Mortar",
        "sound_desc": "곡식을 넣고 빻는 돌절구 모양",
        "example_word": "臼齒 (구치)",
        "example_word_desc": "음식을 으깨는 어금니 (Molar tooth)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">臼</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "杵": {
        "char": "杵",
        "stroke_count": 8,
        "hun_eum": "공이 처",
        "hun_eum_en": "Pestle",
        "sound_desc": "절구통 속을 찧는 방망이 공이 모양",
        "example_word": "杵臼 (처구)",
        "example_word_desc": "방망이와 절구 (Mortar and pestle)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">杵</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "箕": {
        "char": "箕",
        "stroke_count": 14,
        "hun_eum": "키 기",
        "hun_eum_en": "Winnow, Basket",
        "sound_desc": "곡식의 쭉정이를 까부르는 대나무 키 모양",
        "example_word": "箕宿 (기수)",
        "example_word_desc": "별자리 이름 (Constellation)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">箕</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "帚": {
        "char": "帚",
        "stroke_count": 8,
        "hun_eum": "비 추",
        "hun_eum_en": "Broom",
        "sound_desc": "짚이나 싸리나무를 묶은 빗자루 모양",
        "example_word": "掃帚 (소추)",
        "example_word_desc": "먼지를 쓸어내는 빗자루 (Broom)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">帚</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "卓": {
        "char": "卓",
        "stroke_count": 8,
        "hun_eum": "탁자 탁",
        "hun_eum_en": "Table, High",
        "sound_desc": "높직하게 다리를 세운 탁자 모양",
        "example_word": "卓球 (탁구)",
        "example_word_desc": "탁자 위에서 치는 핑퐁 (Table tennis)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">卓</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "几": {
        "char": "几",
        "stroke_count": 2,
        "hun_eum": "안석 궤",
        "hun_eum_en": "Table, Stool",
        "sound_desc": "몸을 편안히 기대는 작은 탁자 모양",
        "example_word": "茶几 (다궤)",
        "example_word_desc": "찻잔을 올려놓는 작은 상 (Tea table)",
        "stroke_names": ["1번째 획!", "2번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">几</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "床": {
        "char": "床",
        "stroke_count": 7,
        "hun_eum": "평상 상",
        "hun_eum_en": "Bed, Floor",
        "sound_desc": "다리가 달린 평상과 마루 모양",
        "example_word": "臥床 (와상)",
        "example_word_desc": "편안히 누워 쉬는 침상 (Bed)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">床</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "繩": {
        "char": "繩",
        "stroke_count": 19,
        "hun_eum": "줄 승",
        "hun_eum_en": "Rope, Cord",
        "sound_desc": "실을 꼬아 만든 튼튼한 밧줄 모양",
        "example_word": "繩索 (승삭)",
        "example_word_desc": "물건을 묶는 밧줄 (Rope)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!", "17번째 획!", "18번째 획!", "19번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">繩</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "索": {
        "char": "索",
        "stroke_count": 10,
        "hun_eum": "노 삭",
        "hun_eum_en": "Rope, Search",
        "sound_desc": "새끼줄을 꼬는 손 모양에서 줄과 찾음의 뜻",
        "example_word": "索引 (색인)",
        "example_word_desc": "원하는 항목을 찾는 인덱스 (Index)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">索</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "針": {
        "char": "針",
        "stroke_count": 10,
        "hun_eum": "바늘 침",
        "hun_eum_en": "Needle, Pin",
        "sound_desc": "실을 꿰는 뾰족한 쇠바늘 모양",
        "example_word": "針灸 (침구)",
        "example_word_desc": "한의학의 침과 뜸 (Acupuncture)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">針</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鏡": {
        "char": "鏡",
        "stroke_count": 19,
        "hun_eum": "거울 경",
        "hun_eum_en": "Mirror, Lens",
        "sound_desc": "쇠를 반짝이게 갈아 얼굴을 비추는 거울 모양",
        "example_word": "鏡台 (경대)",
        "example_word_desc": "거울이 달린 화장대 (Dressing table)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!", "17번째 획!", "18번째 획!", "19번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鏡</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鐘": {
        "char": "鐘",
        "stroke_count": 20,
        "hun_eum": "종 종",
        "hun_eum_en": "Bell, Clock",
        "sound_desc": "쇠로 주조하여 맑은 소리를 내는 큰 종 모양",
        "example_word": "鐘閣 (종각)",
        "example_word_desc": "보신각처럼 종을 걸어둔 누각 (Bell tower)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!", "17번째 획!", "18번째 획!", "19번째 획!", "20번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鐘</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鼓": {
        "char": "鼓",
        "stroke_count": 13,
        "hun_eum": "북 고",
        "hun_eum_en": "Drum, Beat",
        "sound_desc": "가죽을 팽팽히 씌운 북을 채로 치는 모양",
        "example_word": "鼓動 (고동)",
        "example_word_desc": "심장이 힘차게 뛰는 박동 (Heartbeat)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鼓</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "磬": {
        "char": "磬",
        "stroke_count": 16,
        "hun_eum": "경쇠 경",
        "hun_eum_en": "Chime stone",
        "sound_desc": "돌을 깎아 매달고 치는 악기 경쇠 모양",
        "example_word": "編磬 (편경)",
        "example_word_desc": "궁중 음악에 쓰이는 타악기 (Stone chimes)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">磬</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "笛": {
        "char": "笛",
        "stroke_count": 11,
        "hun_eum": "피리 적",
        "hun_eum_en": "Flute, Pipe",
        "sound_desc": "대나무에 구멍을 뚫어 부는 피리 모양",
        "example_word": "笛聲 (적성)",
        "example_word_desc": "청아하게 울리는 피리 소리 (Flute sound)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">笛</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "琴": {
        "char": "琴",
        "stroke_count": 12,
        "hun_eum": "거문고 금",
        "hun_eum_en": "Zither, Piano",
        "sound_desc": "줄을 튕겨 아름다운 음을 내는 거문고 모양",
        "example_word": "琴線 (금선)",
        "example_word_desc": "마음을 울리는 거문고 줄 (Heartstrings)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">琴</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "管": {
        "char": "管",
        "stroke_count": 14,
        "hun_eum": "대롱 관",
        "hun_eum_en": "Pipe, Tube",
        "sound_desc": "속이 텅 빈 대나무 대롱 모양",
        "example_word": "管理 (관리)",
        "example_word_desc": "시설과 조직을 보살핌 (Management)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">管</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "印": {
        "char": "印",
        "stroke_count": 6,
        "hun_eum": "도장 인",
        "hun_eum_en": "Seal, Stamp",
        "sound_desc": "손으로 도장을 꾹 누르는 모양",
        "example_word": "印鑑 (인감)",
        "example_word_desc": "공식적으로 등록한 도장 (Official seal)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">印</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "楯": {
        "char": "楯",
        "stroke_count": 13,
        "hun_eum": "방패 순",
        "hun_eum_en": "Shield",
        "sound_desc": "적의 화살과 창을 막는 나무 방패 모양",
        "example_word": "矛盾 (모순)",
        "example_word_desc": "어떤 창도 뚫지 못하는 방패 (Shield)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">楯</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
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
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">門</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "戶": {
        "char": "戶",
        "stroke_count": 4,
        "hun_eum": "지게문 호",
        "hun_eum_en": "Door, Household",
        "sound_desc": "외짝으로 여닫는 방문 모양",
        "example_word": "戶籍 (호적)",
        "example_word_desc": "집안의 가족 명부 (Family registry)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">戶</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "宮": {
        "char": "宮",
        "stroke_count": 10,
        "hun_eum": "집 궁",
        "hun_eum_en": "Palace",
        "sound_desc": "기둥과 지붕이 웅장하게 연결된 궁궐 모양",
        "example_word": "宮闕 (궁궐)",
        "example_word_desc": "임금님이 사시는 대궐 (Royal palace)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">宮</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "室": {
        "char": "室",
        "stroke_count": 9,
        "hun_eum": "집 실",
        "hun_eum_en": "Room, Chamber",
        "sound_desc": "지붕 아래 사람이 편히 머무는 방 모양",
        "example_word": "敎室 (교실)",
        "example_word_desc": "선생님과 공부하는 방 (Classroom)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">室</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "堂": {
        "char": "堂",
        "stroke_count": 11,
        "hun_eum": "집 당",
        "hun_eum_en": "Hall, Shrine",
        "sound_desc": "높은 축대 위에 지은 의젓한 큰 집 모양",
        "example_word": "堂堂 (당당)",
        "example_word_desc": "남앞에 떳떳하고 늠름함 (Confident)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">堂</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "屋": {
        "char": "屋",
        "stroke_count": 9,
        "hun_eum": "집 옥",
        "hun_eum_en": "House, Roof",
        "sound_desc": "지붕이 덮인 안락한 집 모양",
        "example_word": "屋上 (옥상)",
        "example_word_desc": "건물의 맨 꼭대기 지붕 (Rooftop)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">屋</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "衣": {
        "char": "衣",
        "stroke_count": 6,
        "hun_eum": "옷 의",
        "hun_eum_en": "Clothes, Dress",
        "sound_desc": "목깃과 소매, 옷자락이 달린 겉옷 모양",
        "example_word": "衣服 (의복)",
        "example_word_desc": "몸에 걸치는 모든 옷 (Clothes)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">衣</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "巾": {
        "char": "巾",
        "stroke_count": 3,
        "hun_eum": "수건 건",
        "hun_eum_en": "Cloth, Towel",
        "sound_desc": "허리춤에 걸쳐 늘어뜨린 수건 천 모양",
        "example_word": "手巾 (수건)",
        "example_word_desc": "손과 얼굴을 닦는 천 (Hand towel)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">巾</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "帶": {
        "char": "帶",
        "stroke_count": 11,
        "hun_eum": "띠 대",
        "hun_eum_en": "Belt, Zone",
        "sound_desc": "허리에 두르는 장식 띠 모양",
        "example_word": "帶狀 (대상)",
        "example_word_desc": "띠처럼 길게 이어진 형태 (Belt shape)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">帶</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "履": {
        "char": "履",
        "stroke_count": 15,
        "hun_eum": "신 리",
        "hun_eum_en": "Shoes, Walk",
        "sound_desc": "발에 신고 걸어 다니는 가죽신 모양",
        "example_word": "履歷 (이력)",
        "example_word_desc": "살아오며 밟아온 발자취 (Resume, Career)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">履</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "冠": {
        "char": "冠",
        "stroke_count": 9,
        "hun_eum": "갓 관",
        "hun_eum_en": "Crown, Cap",
        "sound_desc": "머리에 단정하게 쓰는 갓과 관 모양",
        "example_word": "王冠 (왕관)",
        "example_word_desc": "임금이 머리에 쓰는 관 (Royal crown)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">冠</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "傘": {
        "char": "傘",
        "stroke_count": 12,
        "hun_eum": "우산 산",
        "hun_eum_en": "Umbrella",
        "sound_desc": "살대를 펴서 비를 가리는 우산 모양",
        "example_word": "雨傘 (우산)",
        "example_word_desc": "비를 막는 접이식 산 (Umbrella)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">傘</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "食": {
        "char": "食",
        "stroke_count": 9,
        "hun_eum": "밥 식",
        "hun_eum_en": "Eat, Food",
        "sound_desc": "뚜껑이 덮인 밥그릇에 수북한 음식 모양",
        "example_word": "食堂 (식당)",
        "example_word_desc": "맛있는 밥을 먹는 집 (Restaurant)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">食</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "酒": {
        "char": "酒",
        "stroke_count": 10,
        "hun_eum": "술 주",
        "hun_eum_en": "Alcohol, Wine",
        "sound_desc": "술병에서 향기로운 술이 떨어지는 모양",
        "example_word": "酒母 (주모)",
        "example_word_desc": "주막에서 술을 파는 여주인 (Bar hostess)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">酒</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "酉": {
        "char": "酉",
        "stroke_count": 7,
        "hun_eum": "술병 유",
        "hun_eum_en": "Wine vessel",
        "sound_desc": "향기로운 술을 발효시키는 단지 모양",
        "example_word": "酉時 (유시)",
        "example_word_desc": "오후 5시에서 7시 사이 (5 to 7 PM)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">酉</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "鬯": {
        "char": "鬯",
        "stroke_count": 10,
        "hun_eum": "울창주 창",
        "hun_eum_en": "Sacrificial Wine",
        "sound_desc": "제사에 올리는 향기로운 술그릇 모양",
        "example_word": "鬯酒 (창주)",
        "example_word_desc": "제사용 향기로운 술 (Sacrificial wine)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">鬯</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "冊": {
        "char": "冊",
        "stroke_count": 5,
        "hun_eum": "책 책",
        "hun_eum_en": "Book, Volume",
        "sound_desc": "대나무 조각을 끈으로 엮은 죽간 책 모양",
        "example_word": "冊床 (책상)",
        "example_word_desc": "책을 펴놓고 공부하는 상 (Desk)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">冊</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "聿": {
        "char": "聿",
        "stroke_count": 6,
        "hun_eum": "붓 율",
        "hun_eum_en": "Brush",
        "sound_desc": "손에 붓을 바르게 쥐고 글씨를 쓰는 모양",
        "example_word": "聿部 (율부)",
        "example_word_desc": "붓 관련 한자 부수 (Brush radical)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">聿</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "筆": {
        "char": "筆",
        "stroke_count": 12,
        "hun_eum": "붓 필",
        "hun_eum_en": "Brush, Pen",
        "sound_desc": "대나무 대에 짐승 털을 꽂은 붓 모양",
        "example_word": "筆記 (필기)",
        "example_word_desc": "글씨를 써서 기록함 (Note taking)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">筆</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "墨": {
        "char": "墨",
        "stroke_count": 15,
        "hun_eum": "먹 묵",
        "hun_eum_en": "Ink, Black",
        "sound_desc": "그을음과 흙을 뭉쳐 만든 검은 먹 모양",
        "example_word": "水墨 (수묵)",
        "example_word_desc": "물과 먹으로 그린 그림 (Ink painting)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">墨</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "紙": {
        "char": "紙",
        "stroke_count": 10,
        "hun_eum": "종이 지",
        "hun_eum_en": "Paper",
        "sound_desc": "닥나무 섬유를 물에 풀어 뜬 종이 모양",
        "example_word": "紙面 (지면)",
        "example_word_desc": "신문이나 책의 인쇄면 (Page, Paper)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">紙</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "硯": {
        "char": "硯",
        "stroke_count": 12,
        "hun_eum": "벼루 연",
        "hun_eum_en": "Inkstone",
        "sound_desc": "먹을 갈아 먹물을 내는 넓적한 돌벼루 모양",
        "example_word": "硯滴 (연적)",
        "example_word_desc": "벼루에 물을 붓는 주전자 (Water dropper)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">硯</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "錢": {
        "char": "錢",
        "stroke_count": 16,
        "hun_eum": "돈 전",
        "hun_eum_en": "Money, Coin",
        "sound_desc": "쇠로 주조한 동전 엽전 모양",
        "example_word": "金錢 (금전)",
        "example_word_desc": "물건을 사고파는 돈 (Money)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">錢</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "玉": {
        "char": "玉",
        "stroke_count": 5,
        "hun_eum": "구슬 옥",
        "hun_eum_en": "Jade, Jewel",
        "sound_desc": "세 개의 영롱한 옥구슬을 실로 꿴 모양",
        "example_word": "玉石 (옥석)",
        "example_word_desc": "옥과 보통 돌 (Jade and stone)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">玉</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "瓦": {
        "char": "瓦",
        "stroke_count": 5,
        "hun_eum": "기와 와",
        "hun_eum_en": "Tile, Roof tile",
        "sound_desc": "지붕에 나란히 얹은 진흙 기와 모양",
        "example_word": "瓦家 (와가)",
        "example_word_desc": "기와로 지붕을 인 기와집 (Tiled house)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">瓦</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "郭": {
        "char": "郭",
        "stroke_count": 11,
        "hun_eum": "성곽 곽",
        "hun_eum_en": "Outer wall, Castle",
        "sound_desc": "도성을 둘러싼 튼튼한 성곽 모양",
        "example_word": "城郭 (성곽)",
        "example_word_desc": "도시를 방어하는 성벽 (Castle wall)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">郭</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
    "壘": {
        "char": "壘",
        "stroke_count": 18,
        "hun_eum": "보루 루",
        "hun_eum_en": "Fort, Base",
        "sound_desc": "흙과 돌을 쌓아 올린 군사 진지 모양",
        "example_word": "堡壘 (보루)",
        "example_word_desc": "적을 막는 튼튼한 진지 (Stronghold)",
        "stroke_names": ["1번째 획!", "2번째 획!", "3번째 획!", "4번째 획!", "5번째 획!", "6번째 획!", "7번째 획!", "8번째 획!", "9번째 획!", "10번째 획!", "11번째 획!", "12번째 획!", "13번째 획!", "14번째 획!", "15번째 획!", "16번째 획!", "17번째 획!", "18번째 획!"],
        "drawing_svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <rect x="64" y="64" width="896" height="896" rx="160" fill="#FEF3C7" stroke="#F59E0B" stroke-width="28"/>
  <circle cx="512" cy="512" r="320" fill="#FDE68A" opacity="0.5"/>
  <text x="512" y="580" font-size="340" font-family="Batang, serif" font-weight="bold" fill="#B45309" text-anchor="middle">壘</text>
  <circle cx="240" cy="240" r="40" fill="#EF4444" opacity="0.7"/>
  <circle cx="784" cy="784" r="40" fill="#3B82F6" opacity="0.7"/>
</svg>"""
    },
}
