"""
160개 상형한자 최적화 컬러 벡터 일러스트(SVG) 전면 업그레이드 생성기
- 한자의 본래 뜻(상형 기원 및 의미)과 직관적으로 100% 일치하는 고품질 벡터 일러스트 구성
- Twemoji / OpenMoji 최적 코드 선별 및 특수 상형문자 전용 커스텀 벡터 일러스트 생성
"""
import os
import sys
import json
import urllib.request

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 1. 특수/상형 의미 전용 맞춤 고품질 벡터 일러스트 생성기
def create_custom_svg(char):
    # 각 한자의 상형적/문화적 고유 의미를 100% 반영한 깔끔한 모던 벡터 그래픽
    custom_assets = {
        # 1) 田 (밭 전): 바둑판 모양의 푸른 논밭/이랑과 벼/작물
        "田": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E8F5E9"/>
  <rect x="56" y="56" width="400" height="400" rx="32" fill="#81C784" stroke="#2E7D32" stroke-width="20"/>
  <!-- 논둑 사분할 -->
  <line x1="256" y1="56" x2="256" y2="456" stroke="#4E342E" stroke-width="24" stroke-linecap="round"/>
  <line x1="56" y1="256" x2="456" y2="256" stroke="#4E342E" stroke-width="24" stroke-linecap="round"/>
  <!-- 밭고랑 작물 새싹들 -->
  <circle cx="156" cy="156" r="28" fill="#2E7D32"/>
  <circle cx="356" cy="156" r="28" fill="#2E7D32"/>
  <circle cx="156" cy="356" r="28" fill="#2E7D32"/>
  <circle cx="356" cy="356" r="28" fill="#2E7D32"/>
  <path d="M156 128 Q140 100 120 110 Q140 135 156 128 Z" fill="#66BB6A"/>
  <path d="M356 128 Q340 100 320 110 Q340 135 356 128 Z" fill="#66BB6A"/>
  <path d="M156 328 Q140 300 120 310 Q140 335 156 328 Z" fill="#66BB6A"/>
  <path d="M356 328 Q340 300 320 310 Q340 335 356 328 Z" fill="#66BB6A"/>
</svg>""",

        # 2) 車 (수레 차): 고대 굴대와 바퀴 살이 달린 목조 수레바퀴/마차
        "車": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF8E1"/>
  <!-- 수레 큰 나무 바퀴 -->
  <circle cx="256" cy="256" r="180" fill="none" stroke="#8D6E63" stroke-width="36"/>
  <circle cx="256" cy="256" r="140" fill="#D7CCC8" opacity="0.3"/>
  <circle cx="256" cy="256" r="45" fill="#5D4037" stroke="#3E2723" stroke-width="12"/>
  <circle cx="256" cy="256" r="18" fill="#FFE082"/>
  <!-- 8개의 바퀴 살 (Spokes) -->
  <line x1="256" y1="76" x2="256" y2="436" stroke="#6D4C41" stroke-width="16"/>
  <line x1="76" y1="256" x2="436" y2="256" stroke="#6D4C41" stroke-width="16"/>
  <line x1="128" y1="128" x2="384" y2="384" stroke="#6D4C41" stroke-width="16"/>
  <line x1="128" y1="384" x2="384" y2="128" stroke="#6D4C41" stroke-width="16"/>
  <!-- 수레 차체 프레임 -->
  <rect x="80" y="240" width="352" height="32" rx="8" fill="#4E342E" opacity="0.85"/>
</svg>""",

        # 3) 井 (우물 정): 정자(井)형 돌틀 우물과 맑은 물
        "井": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E0F7FA"/>
  <!-- 우물 속 깊은 물 -->
  <circle cx="256" cy="256" r="110" fill="#00ACC1"/>
  <circle cx="256" cy="256" r="80" fill="#00838F"/>
  <circle cx="270" cy="240" r="25" fill="#E0F7FA" opacity="0.5"/>
  <!-- 우물 정자(井) 나무/석조 틀 -->
  <!-- 가로 보 2개 -->
  <rect x="60" y="140" width="392" height="52" rx="12" fill="#8D6E63" stroke="#4E342E" stroke-width="10"/>
  <rect x="60" y="320" width="392" height="52" rx="12" fill="#8D6E63" stroke="#4E342E" stroke-width="10"/>
  <!-- 세로 보 2개 -->
  <rect x="140" y="60" width="52" height="392" rx="12" fill="#A1887F" stroke="#4E342E" stroke-width="10"/>
  <rect x="320" y="60" width="52" height="392" rx="12" fill="#A1887F" stroke="#4E342E" stroke-width="10"/>
  <!-- 두레박 줄 -->
  <line x1="256" y1="60" x2="256" y2="250" stroke="#FFB300" stroke-width="8" stroke-dasharray="8 8"/>
</svg>""",

        # 4) 門 (문 문): 웅장한 대궐식 쌍여닫이 대문
        "門": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF3E0"/>
  <!-- 문틀 지붕 및 기둥 -->
  <path d="M40 90 L256 50 L472 90 L450 130 L62 130 Z" fill="#D32F2F" stroke="#5D4037" stroke-width="8"/>
  <rect x="64" y="120" width="40" height="330" fill="#8D6E63" stroke="#3E2723" stroke-width="8"/>
  <rect x="408" y="120" width="40" height="330" fill="#8D6E63" stroke="#3E2723" stroke-width="8"/>
  <!-- 좌측 문짝 -->
  <rect x="110" y="134" width="140" height="310" fill="#B71C1C" stroke="#3E2723" stroke-width="8"/>
  <circle cx="230" cy="280" r="16" fill="#FFD54F" stroke="#FF8F00" stroke-width="4"/>
  <!-- 우측 문짝 -->
  <rect x="262" y="134" width="140" height="310" fill="#C62828" stroke="#3E2723" stroke-width="8"/>
  <circle cx="282" cy="280" r="16" fill="#FFD54F" stroke="#FF8F00" stroke-width="4"/>
  <!-- 문살 장식 -->
  <rect x="130" y="160" width="100" height="80" fill="#880E4F" opacity="0.4"/>
  <rect x="282" y="160" width="100" height="80" fill="#880E4F" opacity="0.4"/>
</svg>""",

        # 5) 戶 (지게문 호): 아늑한 한옥 외짝 방문
        "戶": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FAFAFA"/>
  <!-- 문틀 -->
  <rect x="100" y="60" width="312" height="392" rx="16" fill="#D7CCC8" stroke="#5D4037" stroke-width="16"/>
  <!-- 외짝 문판 -->
  <rect x="124" y="84" width="264" height="344" fill="#FFF9C4" stroke="#8D6E63" stroke-width="10"/>
  <!-- 전통 창살 무늬 -->
  <line x1="124" y1="200" x2="388" y2="200" stroke="#8D6E63" stroke-width="8"/>
  <line x1="124" y1="300" x2="388" y2="300" stroke="#8D6E63" stroke-width="8"/>
  <line x1="210" y1="84" x2="210" y2="428" stroke="#8D6E63" stroke-width="8"/>
  <line x1="300" y1="84" x2="300" y2="428" stroke="#8D6E63" stroke-width="8"/>
  <!-- 문고리 배꼽 -->
  <circle cx="160" cy="256" r="18" fill="#FFB300" stroke="#E65100" stroke-width="4"/>
  <path d="M160 270 L160 305" stroke="#E65100" stroke-width="8" stroke-linecap="round"/>
</svg>""",

        # 6) 鼎 (솥 정): 고대 청동 세 발 솥 (구구정 형태의 웅장한 제기)
        "鼎": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#ECEFF1"/>
  <!-- 솥 몸통 귀 (좌우 손잡이) -->
  <path d="M100 130 L100 80 Q100 60 120 60 L140 60 L140 130" fill="none" stroke="#37474F" stroke-width="20"/>
  <path d="M412 130 L412 80 Q412 60 392 60 L372 60 L372 130" fill="none" stroke="#37474F" stroke-width="20"/>
  <!-- 솥 몸체 -->
  <path d="M90 130 Q90 320 256 330 Q422 320 422 130 Z" fill="#546E7A" stroke="#263238" stroke-width="16"/>
  <!-- 고대 청동기 무늬 띠 -->
  <rect x="100" y="160" width="312" height="40" rx="8" fill="#78909C"/>
  <circle cx="160" cy="180" r="10" fill="#CFD8DC"/>
  <circle cx="256" cy="180" r="10" fill="#CFD8DC"/>
  <circle cx="352" cy="180" r="10" fill="#CFD8DC"/>
  <!-- 세 다리 (Tripod legs) -->
  <path d="M130 310 L100 450" stroke="#37474F" stroke-width="32" stroke-linecap="round"/>
  <path d="M256 325 L256 460" stroke="#263238" stroke-width="34" stroke-linecap="round"/>
  <path d="M382 310 L412 450" stroke="#37474F" stroke-width="32" stroke-linecap="round"/>
</svg>""",

        # 7) 戈 (창 과) / 矛 (창 모): 고대 꺾창과 찌르는 장창
        "戈": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FBE9E7"/>
  <!-- 긴 창 자루 (나무) -->
  <line x1="80" y1="440" x2="380" y2="100" stroke="#5D4037" stroke-width="22" stroke-linecap="round"/>
  <!-- 꺾인 청동 날 (ㄱ자 꺾창) -->
  <path d="M350 130 L450 70 L430 160 L380 180 Z" fill="#78909C" stroke="#263238" stroke-width="10"/>
  <!-- 아래로 향한 갈고리 날 -->
  <path d="M330 150 L270 230 L310 240 Z" fill="#90A4AE" stroke="#263238" stroke-width="8"/>
  <!-- 붉은 술 장식 -->
  <circle cx="350" cy="140" r="18" fill="#D32F2F"/>
  <path d="M350 140 Q330 190 320 220" stroke="#D32F2F" stroke-width="8" stroke-linecap="round"/>
</svg>""",

        "矛": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#ECEFF1"/>
  <!-- 긴 장창 자루 -->
  <line x1="90" y1="422" x2="360" y2="152" stroke="#4E342E" stroke-width="20" stroke-linecap="round"/>
  <!-- 날카로운 양날 창끝 -->
  <path d="M340 170 Q430 100 460 52 Q412 142 362 192 Z" fill="#B0BEC5" stroke="#263238" stroke-width="10"/>
  <line x1="350" y1="180" x2="455" y2="57" stroke="#ECEFF1" stroke-width="6"/>
  <!-- 붉은 깃발/술 장식 -->
  <path d="M330 180 Q310 240 280 260 Q320 230 350 200 Z" fill="#C62828"/>
</svg>""",

        # 8) 印 (도장 인): 붉은 인주가 묻은 사각 옥새/도장과 낙관
        "印": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFEBEE"/>
  <!-- 도장 본체 (사각 인장) -->
  <path d="M180 80 L332 80 L360 260 L152 260 Z" fill="#D7CCC8" stroke="#5D4037" stroke-width="14"/>
  <ellipse cx="256" cy="80" rx="76" ry="30" fill="#BCAAA4" stroke="#5D4037" stroke-width="12"/>
  <!-- 도장 바닥 인면 (붉은 인주) -->
  <rect x="140" y="260" width="232" height="40" rx="8" fill="#D32F2F" stroke="#B71C1C" stroke-width="8"/>
  <!-- 찍힌 사각 붉은 낙관 도장 자국 -->
  <rect x="176" y="340" width="160" height="120" rx="16" fill="none" stroke="#C62828" stroke-width="16"/>
  <path d="M210 370 L240 430 M240 370 L210 430 M280 370 L280 430 M265 400 L305 400" stroke="#C62828" stroke-width="12" stroke-linecap="round"/>
</svg>""",

        # 9) 網 (그물 망): 물고기를 잡는 그물망
        "網": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E1F5FE"/>
  <!-- 둥근 그물 테두리 로프 -->
  <path d="M80 120 Q256 60 432 120 Q410 420 256 450 Q102 420 80 120 Z" fill="#81D4FA" opacity="0.3" stroke="#0277BD" stroke-width="14"/>
  <!-- 그물 격자선 대각선 1 -->
  <path d="M120 110 L390 380 M180 90 L420 330 M260 80 L430 250 M85 180 L330 430 M95 270 L250 445" stroke="#01579B" stroke-width="8"/>
  <!-- 그물 격자선 대각선 2 -->
  <path d="M390 110 L120 380 M330 90 L90 330 M250 80 L80 250 M425 180 L180 430 M415 270 L260 445" stroke="#01579B" stroke-width="8"/>
  <!-- 그물 추 (납작한 도토리 추) -->
  <circle cx="100" cy="380" r="14" fill="#455A64"/>
  <circle cx="170" cy="425" r="14" fill="#455A64"/>
  <circle cx="256" cy="450" r="14" fill="#455A64"/>
  <circle cx="342" cy="425" r="14" fill="#455A64"/>
  <circle cx="412" cy="380" r="14" fill="#455A64"/>
</svg>""",

        # 10) 缶 (장군/항아리 부): 흙으로 빚은 도자기 옹기/장군
        "缶": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#EFEBE9"/>
  <!-- 도자기 주둥이 -->
  <ellipse cx="256" cy="110" rx="90" ry="24" fill="#8D6E63" stroke="#4E342E" stroke-width="12"/>
  <ellipse cx="256" cy="110" rx="60" ry="14" fill="#3E2723"/>
  <!-- 불룩한 몸체 -->
  <path d="M170 120 C100 180 80 280 120 380 C140 430 200 450 256 450 C312 450 372 430 392 380 C432 280 412 180 342 120 Z" fill="#6D4C41" stroke="#3E2723" stroke-width="16"/>
  <!-- 옹기 장식 무늬 -->
  <path d="M120 280 Q256 340 392 280" fill="none" stroke="#A1887F" stroke-width="12" stroke-linecap="round"/>
  <path d="M140 240 Q256 300 372 240" fill="none" stroke="#D7CCC8" stroke-width="8" stroke-dasharray="12 12"/>
</svg>""",

        # 11) 瓦 (기와 와): 전통 한옥 지붕 기와
        "瓦": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#ECEFF1"/>
  <!-- 겹쳐진 둥근 암키와와 수키와 골 -->
  <!-- 바탕 수키와 곡선들 -->
  <path d="M80 360 C80 260 160 260 160 360 L140 440 L60 440 Z" fill="#546E7A" stroke="#263238" stroke-width="10"/>
  <path d="M216 360 C216 260 296 260 296 360 L276 440 L196 440 Z" fill="#546E7A" stroke="#263238" stroke-width="10"/>
  <path d="M352 360 C352 260 432 260 432 360 L412 440 L332 440 Z" fill="#546E7A" stroke="#263238" stroke-width="10"/>
  <!-- 상단 기와 등마루 -->
  <ellipse cx="120" cy="270" rx="42" ry="24" fill="#78909C" stroke="#263238" stroke-width="8"/>
  <ellipse cx="256" cy="270" rx="42" ry="24" fill="#78909C" stroke="#263238" stroke-width="8"/>
  <ellipse cx="392" cy="270" rx="42" ry="24" fill="#78909C" stroke="#263238" stroke-width="8"/>
  <!-- 전통 수막새 와당 연꽃 무늬 -->
  <circle cx="256" cy="270" r="12" fill="#CFD8DC"/>
  <!-- 상단 처마 라인 -->
  <path d="M40 220 Q256 160 472 220 L450 170 Q256 120 62 170 Z" fill="#37474F" stroke="#212121" stroke-width="10"/>
</svg>""",

        # 12) 管 (대롱 관): 마디가 뚜렷한 대나무 대롱/피리관
        "管": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#F1F8E9"/>
  <!-- 대나무 파이프 본체 -->
  <rect x="180" y="50" width="152" height="412" rx="20" fill="#8BC34A" stroke="#33691E" stroke-width="14"/>
  <!-- 속이 빈 대롱 입구 -->
  <ellipse cx="256" cy="70" rx="56" ry="20" fill="#558B2F" stroke="#33691E" stroke-width="8"/>
  <ellipse cx="256" cy="70" rx="36" ry="12" fill="#1B5E20"/>
  <!-- 대나무 마디들 -->
  <rect x="164" y="160" width="184" height="24" rx="10" fill="#689F38" stroke="#33691E" stroke-width="8"/>
  <rect x="164" y="280" width="184" height="24" rx="10" fill="#689F38" stroke="#33691E" stroke-width="8"/>
  <rect x="164" y="400" width="184" height="24" rx="10" fill="#689F38" stroke="#33691E" stroke-width="8"/>
  <!-- 대나무 잎 장식 -->
  <path d="M340 170 Q420 140 440 180 Q390 190 340 175 Z" fill="#4CAF50"/>
</svg>""",

        # 13) 琴 (거문고/가야금 금): 줄이 팽팽하게 얹힌 전통 명품 현악기
        "琴": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFFDE7"/>
  <!-- 오동나무 공명판 울림통 -->
  <rect x="120" y="50" width="272" height="412" rx="30" fill="#8D6E63" stroke="#4E342E" stroke-width="16"/>
  <ellipse cx="256" cy="256" rx="32" ry="16" fill="#3E2723"/>
  <!-- 7현 현악기 줄 (Strings) -->
  <line x1="160" y1="60" x2="160" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="192" y1="60" x2="192" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="224" y1="60" x2="224" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="256" y1="60" x2="256" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="288" y1="60" x2="288" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="320" y1="60" x2="320" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="352" y1="60" x2="352" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <!-- 줄을 받치는 안족(기러기발) 브릿지 -->
  <path d="M150 160 L170 170 L150 180 Z" fill="#FFE082"/>
  <path d="M182 200 L202 210 L182 220 Z" fill="#FFE082"/>
  <path d="M214 240 L234 250 L214 260 Z" fill="#FFE082"/>
  <path d="M246 280 L266 290 L246 300 Z" fill="#FFE082"/>
  <path d="M278 320 L298 330 L278 340 Z" fill="#FFE082"/>
  <path d="M310 360 L330 370 L310 380 Z" fill="#FFE082"/>
  <path d="M342 400 L362 410 L342 420 Z" fill="#FFE082"/>
</svg>""",

        # 14) 磬 (경쇠 경): 받침대에 걸려 맑은 소리를 내는 기역자 옥/돌 경쇠 타악기
        "磬": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#F3E5F5"/>
  <!-- 걸이 틀 (프레임) -->
  <rect x="80" y="50" width="352" height="30" rx="8" fill="#5D4037" stroke="#3E2723" stroke-width="8"/>
  <rect x="100" y="70" width="24" height="390" fill="#5D4037"/>
  <rect x="388" y="70" width="24" height="390" fill="#5D4037"/>
  <!-- 끈에 매달린 옥/돌 경쇠 (ㄱ자 꺾인 모양) -->
  <line x1="200" y1="80" x2="200" y2="160" stroke="#D32F2F" stroke-width="8"/>
  <line x1="312" y1="80" x2="312" y2="160" stroke="#D32F2F" stroke-width="8"/>
  <path d="M140 200 L256 160 L372 260 L340 320 L256 240 L160 270 Z" fill="#80CBC4" stroke="#004D40" stroke-width="14"/>
  <!-- 타악 채 -->
  <line x1="320" y1="360" x2="420" y2="280" stroke="#FFB300" stroke-width="12" stroke-linecap="round"/>
  <circle cx="320" cy="360" r="20" fill="#D32F2F"/>
</svg>""",

        # 15) 森 (나무빽빽할 삼): 3그루의 나무가 울창하게 우거진 숲
        "森": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E8F5E9"/>
  <!-- 상단 중앙 나무 -->
  <rect x="242" y="160" width="28" height="90" fill="#795548"/>
  <circle cx="256" cy="130" r="65" fill="#2E7D32"/>
  <circle cx="230" cy="120" r="45" fill="#43A047"/>
  <!-- 좌하단 나무 -->
  <rect x="142" y="340" width="28" height="100" fill="#795548"/>
  <circle cx="156" cy="300" r="75" fill="#1B5E20"/>
  <circle cx="130" cy="280" r="55" fill="#388E3C"/>
  <!-- 우하단 나무 -->
  <rect x="342" y="340" width="28" height="100" fill="#795548"/>
  <circle cx="356" cy="300" r="75" fill="#2E7D32"/>
  <circle cx="380" cy="280" r="55" fill="#4CAF50"/>
</svg>""",

        # 16) 林 (수풀 림): 2그루의 나무가 나란히 선 숲
        "林": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E8F8F5"/>
  <!-- 좌측 나무 -->
  <rect x="156" y="270" width="32" height="160" fill="#6D4C41"/>
  <circle cx="172" cy="210" r="95" fill="#2E7D32"/>
  <circle cx="145" cy="185" r="70" fill="#43A047"/>
  <!-- 우측 나무 -->
  <rect x="324" y="270" width="32" height="160" fill="#6D4C41"/>
  <circle cx="340" cy="210" r="95" fill="#388E3C"/>
  <circle cx="365" cy="185" r="70" fill="#66BB6A"/>
</svg>""",

        # 17) 鬯 (울창주 창): 제사 때 신을 부르기 위해 향기로운 풀을 넣은 제사용 술 항아리와 국자
        "鬯": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF8E1"/>
  <!-- 술 그릇 몸통 -->
  <path d="M120 180 L392 180 L350 420 L162 420 Z" fill="#D7CCC8" stroke="#4E342E" stroke-width="16"/>
  <!-- 향긋한 울금 풀 잎들 -->
  <path d="M220 200 Q200 130 160 140 Q180 190 220 200 Z" fill="#4CAF50"/>
  <path d="M292 200 Q312 130 352 140 Q332 190 292 200 Z" fill="#66BB6A"/>
  <!-- 황금빛 향기 술방울 -->
  <circle cx="256" cy="300" r="40" fill="#FFC107" stroke="#FFA000" stroke-width="8"/>
  <circle cx="256" cy="300" r="20" fill="#FFE082"/>
  <!-- 술 뜨는 긴 옥국자 손잡이 -->
  <line x1="256" y1="300" x2="380" y2="80" stroke="#00796B" stroke-width="14" stroke-linecap="round"/>
</svg>""",

        # 18) 鬲 (솥 력): 세 발 달린 고대 토기 솥
        "鬲": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#EFEBE9"/>
  <!-- 입구 전 -->
  <rect x="140" y="100" width="232" height="36" rx="8" fill="#8D6E63" stroke="#4E342E" stroke-width="12"/>
  <!-- 불룩한 몸체와 주머니 모양 세 발 -->
  <path d="M150 136 C100 220 80 320 120 440 L170 440 C190 350 210 320 256 320 C302 320 322 350 342 440 L392 440 C432 320 412 220 362 136 Z" fill="#A1887F" stroke="#4E342E" stroke-width="16"/>
  <!-- 토기 무늬 새김선 -->
  <line x1="160" y1="210" x2="352" y2="210" stroke="#4E342E" stroke-width="8" stroke-dasharray="12 12"/>
  <line x1="180" y1="260" x2="332" y2="260" stroke="#4E342E" stroke-width="8" stroke-dasharray="12 12"/>
</svg>""",

        # 19) 原 (언덕/근원 원): 바위 언덕 아래 맑은 샘물이 콸콸 솟아오르는 원천
        "原": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E0F2F1"/>
  <!-- 깎아지른 바위 언덕(厂) -->
  <path d="M60 80 L440 80 L440 140 L160 140 L160 440 L60 440 Z" fill="#78909C" stroke="#37474F" stroke-width="14"/>
  <!-- 샘물이 솟아나는 옹달샘(泉) -->
  <circle cx="310" cy="270" r="70" fill="#00B0FF" stroke="#0091EA" stroke-width="12"/>
  <circle cx="310" cy="270" r="45" fill="#E1F5FE"/>
  <!-- 솟구치는 물줄기 파동 -->
  <path d="M310 270 Q380 340 430 420" fill="none" stroke="#00B0FF" stroke-width="14" stroke-linecap="round"/>
  <path d="M280 310 Q310 380 340 440" fill="none" stroke="#40C4FF" stroke-width="12" stroke-linecap="round"/>
  <circle cx="340" cy="220" r="14" fill="#00B0FF"/>
</svg>""",

        # 20) 臼 (절구 구) & 杵 (공이 처)
        "臼": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFFDE7"/>
  <!-- 통나무 절구통 외형 -->
  <path d="M120 120 L392 120 C360 240 380 360 400 440 L112 440 C132 360 152 240 120 120 Z" fill="#8D6E63" stroke="#4E342E" stroke-width="16"/>
  <!-- 절구 안 오목한 곡식 찧는 홈 -->
  <ellipse cx="256" cy="140" rx="120" ry="40" fill="#D7CCC8" stroke="#4E342E" stroke-width="10"/>
  <ellipse cx="256" cy="140" rx="90" ry="25" fill="#5D4037"/>
  <!-- 절구 속 하얀 쌀/곡식 알갱이들 -->
  <circle cx="240" cy="140" r="8" fill="#FFFFFF"/>
  <circle cx="265" cy="142" r="7" fill="#FFFFFF"/>
  <circle cx="252" cy="135" r="6" fill="#FFFFFF"/>
</svg>""",

        "杵": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFFDE7"/>
  <!-- 절구 방망이 (양 끝이 굵고 가운데가 잘록한 전통 공이) -->
  <path d="M226 60 L286 60 Q270 200 266 256 Q270 312 286 452 L226 452 Q242 312 246 256 Q242 200 226 60 Z" fill="#A1887F" stroke="#4E342E" stroke-width="14"/>
  <!-- 공이 타격부 링 장식 -->
  <ellipse cx="256" cy="70" rx="30" ry="10" fill="#6D4C41"/>
  <ellipse cx="256" cy="442" rx="30" ry="10" fill="#6D4C41"/>
</svg>""",

        # 21) 箕 (키 기): 곡식의 티끌을 까부르는 대나무 키
        "箕": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF9C4"/>
  <!-- ㄷ자형 대나무 키 바닥 판 -->
  <path d="M100 100 L412 100 L370 420 L142 420 Z" fill="#FFE082" stroke="#FF8F00" stroke-width="16"/>
  <!-- 뒤쪽 높은 테두리 -->
  <path d="M100 100 Q256 60 412 100 L400 140 Q256 100 112 140 Z" fill="#FFA000"/>
  <!-- 대나무 엮음 살무늬 -->
  <line x1="130" y1="180" x2="382" y2="180" stroke="#FFB300" stroke-width="8"/>
  <line x1="140" y1="260" x2="372" y2="260" stroke="#FFB300" stroke-width="8"/>
  <line x1="150" y1="340" x2="362" y2="340" stroke="#FFB300" stroke-width="8"/>
  <line x1="200" y1="120" x2="190" y2="410" stroke="#FFB300" stroke-width="8"/>
  <line x1="256" y1="100" x2="256" y2="415" stroke="#FF8F00" stroke-width="10"/>
  <line x1="312" y1="120" x2="322" y2="410" stroke="#FFB300" stroke-width="8"/>
</svg>""",

        # 22) 皮 (가죽 피): 동물의 털을 벗겨 펴놓은 가죽 원단
        "皮": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#EFEBE9"/>
  <!-- 펼쳐놓은 동물 가죽 윤곽 (네 다리와 꼬리가 있는 호피/우피 형태) -->
  <path d="M220 60 Q256 50 292 60 Q340 100 420 110 Q400 180 360 210 Q420 300 440 390 Q360 400 310 360 Q256 420 202 360 Q152 400 72 390 Q92 300 152 210 Q112 180 92 110 Q172 100 220 60 Z" fill="#D7CCC8" stroke="#5D4037" stroke-width="14"/>
  <!-- 가죽 질감 얼룩무늬 -->
  <ellipse cx="256" cy="220" rx="30" ry="18" fill="#8D6E63"/>
  <ellipse cx="190" cy="280" rx="24" ry="14" fill="#8D6E63"/>
  <ellipse cx="320" cy="280" rx="24" ry="14" fill="#8D6E63"/>
</svg>""",

        # 23) 瓜 (오이 과): 덩굴에 주렁주렁 매달린 참외/오이/박
        "瓜": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#F1F8E9"/>
  <!-- 덩굴 줄기 -->
  <path d="M60 100 Q180 60 256 120 Q340 180 452 110" fill="none" stroke="#558B2F" stroke-width="14" stroke-linecap="round"/>
  <!-- 덩굴손 꼬임 -->
  <path d="M180 80 Q160 30 130 50 Q120 80 150 90" fill="none" stroke="#7CB342" stroke-width="8"/>
  <!-- 매달린 둥글넓적한 노란 참외/박 -->
  <ellipse cx="256" cy="290" rx="120" ry="150" fill="#FDD835" stroke="#F57F17" stroke-width="14"/>
  <!-- 꼭지 -->
  <path d="M256 140 L256 120" stroke="#558B2F" stroke-width="14" stroke-linecap="round"/>
  <!-- 참외 흰 줄무늬들 -->
  <path d="M256 140 Q210 290 256 440" fill="none" stroke="#FFF9C4" stroke-width="10"/>
  <path d="M256 140 Q170 290 216 430" fill="none" stroke="#FFF9C4" stroke-width="10"/>
  <path d="M256 140 Q342 290 296 430" fill="none" stroke="#FFF9C4" stroke-width="10"/>
</svg>""",

        # 24) 燕 (제비 연): 제비 특유의 갈라진 꼬리와 날렵한 날개
        "燕": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E3F2FD"/>
  <!-- 제비 몸통 & 날렵한 날개 -->
  <path d="M256 80 Q290 120 290 200 L440 250 Q300 270 280 340 L340 450 L256 380 L172 450 L232 340 Q212 270 72 250 L222 200 Q222 120 256 80 Z" fill="#263238" stroke="#102027" stroke-width="8"/>
  <!-- 제비 흰 배 -->
  <ellipse cx="256" cy="250" rx="36" ry="60" fill="#ECEFF1"/>
  <!-- 붉은 목덜미 -->
  <circle cx="256" cy="130" r="20" fill="#D32F2F"/>
  <!-- 부리와 눈 -->
  <polygon points="256,50 248,80 264,80" fill="#FFA000"/>
  <circle cx="248" cy="95" r="4" fill="#FFFFFF"/>
  <circle cx="264" cy="95" r="4" fill="#FFFFFF"/>
</svg>""",
    }

    return custom_assets.get(char, None)


# 2. 직관성과 정확성을 100% 극대화한 이모지 & 오픈 벡터 매핑 테이블
OPTIMIZED_DRAWING_MAP = {
    # 1. 자연 & 천문 (15자)
    "日": "2600",      # ☀️ 태양
    "月": "1f319",     # 🌙 초승달
    "山": "26f0",      # ⛰️ 세 봉우리 산
    "水": "1f4a7",     # 💧 맑은 물방울
    "火": "1f525",     # 🔥 활활 타는 불꽃
    "川": "1f3de",     # 🏞️ 흐르는 강/계곡
    "雨": "1f327",     # 🌧️ 비구름과 빗방울
    "土": "1f331",     # 🌱 땅 위의 흙과 새싹
    "石": "1faa8",     # 🪨 단단한 바위/돌
    "風": "1f4a8",     # 💨 바람/돌풍
    "雲": "2601",      # ☁️ 뭉게구름
    "泉": "26f2",      # ⛲ 샘물/분수
    "谷": "1f3de",     # 🏞️ 깊은 산골짜기
    "原": "CUSTOM",    # 🏛️ [CUSTOM] 언덕 아래 샘솟는 원천
    "氣": "1f4a8",     # 💨 피어오르는 기운/김

    # 2. 인체 & 사람 (28자)
    "大": "1f9cd",     # 🧍 팔다리를 크게 벌린 사람
    "人": "1f464",     # 👤 사람의 실루엣
    "女": "1f469",     # 👩 단정한 여인
    "子": "1f476",     # 👶 머리가 큰 갓난아이
    "目": "1f441",     # 👁️ 사람의 눈
    "耳": "1f442",     # 👂 소리를 듣는 귀
    "口": "1f444",     # 👄 열린 입
    "手": "270b",      # ✋ 다섯 손가락 손바닥
    "足": "1f9b6",     # 🦶 종아리와 발바닥
    "心": "2764",      # ❤️ 붉은 심장/마음
    "首": "1f9e0",     # 🧠 머리/우두머리
    "頭": "1f464",     # 👤 사람의 머리통
    "面": "1f600",     # 😀 이목구비가 있는 얼굴
    "齒": "1f9b7",     # 🦷 고르고 단단한 치아
    "舌": "1f445",     # 👅 날름 내민 혀
    "鼻": "1f443",     # 👃 숨 쉬는 코
    "身": "1f9cd",     # 🧍 사람의 온몸 신체
    "骨": "1f9b4",     # 🦴 앙상한 뼈마디
    "肉": "1f356",     # 🍖 뼈에 붙은 붉은 고기
    "血": "1fa78",     # 🩸 붉은 핏방울
    "毛": "1f9b1",     # 🦱 부드러운 털/머리칼
    "皮": "CUSTOM",    # 🐆 [CUSTOM] 벗겨서 펼쳐놓은 동물 가죽
    "爪": "1f485",     # 💅 손끝의 날카로운 손톱
    "角": "1f98c",     # 🦌 솟아난 사슴 뿔
    "母": "1f931",     # 🤱 아기를 품에 안은 어머니
    "父": "1f468",     # 👨 수염 난 다정한 아버지
    "老": "1f474",     # 👴 지팡이를 짚은 노인
    "臣": "1f482",     # 💂 충성스러운 신하

    # 3. 동물 & 곤충 (32자)
    "牛": "1f402",     # 🐂 뿔 달린 황소
    "馬": "1f40e",     # 🐎 갈기 휘날리는 말
    "羊": "1f411",     # 🐑 둥근 뿔의 양
    "豕": "1f416",     # 🐖 뚱뚱한 돼지
    "犬": "1f415",     # 🐕 꼬리 세운 개
    "鳥": "1f426",     # 🐦 부리와 날개 있는 새
    "隹": "1f424",     # 🐤 꼬리가 짧고 통통한 작은 새
    "魚": "1f41f",     # 🐟 비늘과 지느러미 물고기
    "蟲": "1f41b",     # 🐛 꿈틀거리는 벌레
    "龜": "1f422",     # 🐢 등껍질 단단한 거북이
    "象": "1f418",     # 🐘 긴 코 코끼리
    "鹿": "1f98c",     # 🦌 멋진 가지뿔 사슴
    "虎": "1f405",     # 🐅 줄무늬 호랑이
    "蛇": "1f40d",     # 🐍 똬리를 튼 뱀
    "龍": "1f409",     # 🐉 여의주를 문 용
    "羽": "1fab6",     # 🪶 가벼운 새 깃털
    "尾": "1f98a",     # 🦊 풍성한 동물 꼬리
    "兔": "1f407",     # 🐇 긴 귀 토끼
    "鼠": "1f401",     # 🐁 쪼르르 쥐
    "豚": "1f437",     # 🐷 통통한 아기돼지
    "豸": "1f406",     # 🐆 몸을 웅크린 맹수 표범
    "燕": "CUSTOM",    # 🐦 [CUSTOM] 갈라진 제비꼬리 제비
    "貝": "1f41a",     # 🐚 바다 조개껍데기
    "蛙": "1f438",     # 🐸 개구리
    "鶴": "1f9a9",     # 🦩 다리가 긴 두루미/학
    "鵝": "1f9a2",     # 🦢 목이 긴 거위/백조
    "鷹": "1f985",     # 🦅 날카로운 눈빛 매/독수리
    "蜂": "1f41d",     # 🐝 꿀벌
    "蝶": "1f98b",     # 🦋 호랑나비
    "蛛": "1f577",     # 🕷️ 거미
    "蟻": "1f41c",     # 🐜 개미
    "熊": "1f43b",     # 🐻 큰 곰

    # 4. 식물 & 농경 (23자)
    "木": "1f333",     # 🌳 한 그루 나무
    "艸": "1f33f",     # 🌿 풀/약초
    "竹": "1f38b",     # 🎋 대나무 줄기
    "禾": "1f33e",     # 🌾 고개 숙인 벼 이삭
    "米": "1f35a",     # 🍚 하얀 쌀밥
    "果": "1f34e",     # 🍎 나무에 열린 과일 사과
    "瓜": "CUSTOM",    # 🍈 [CUSTOM] 덩굴에 달린 참외/오이
    "桑": "1f343",     # 🍃 뽕나무 잎
    "麥": "1f33e",     # 🌾 보리 이삭
    "麻": "1f9f5",     # 🧵 삼베 실타래
    "豆": "1fac8",     # 🫘 콩 깍지와 콩알
    "黍": "1f33e",     # 🌾 기장 곡식
    "林": "CUSTOM",    # 🌲🌲 [CUSTOM] 2그루 수풀
    "森": "CUSTOM",    # 🌲🌲🌲 [CUSTOM] 3그루 울창한 삼림
    "根": "1f955",     # 🥕 땅속 깊은 뿌리
    "枝": "1fab5",     # 🪵 뻗은 나뭇가지
    "葉": "1f343",     # 🍃 푸른 나뭇잎
    "花": "1f338",     # 🌸 활짝 핀 꽃
    "芽": "1f331",     # 🌱 땅을 뚫고 나온 새싹
    "苗": "1f331",     # 🌱 푸른 모/모종
    "田": "CUSTOM",    # 🟩 [CUSTOM] 바둑판식 논밭이랑
    "井": "CUSTOM",    # 🧱 [CUSTOM] 정자(井)형 돌틀 우물
    "圃": "1f96c",     # 🥬 채소밭

    # 5. 도구 & 무기 (34자)
    "車": "CUSTOM",    # 🛞 [CUSTOM] 바퀴살 달린 옛 목조 수레
    "舟": "26f5",      # ⛵ 물 위의 배
    "刀": "1f5e1",     # 🗡️ 칼/단도
    "弓": "1f3f9",     # 🏹 활과 화살
    "矢": "1f3af",     # 🎯 날아가는 화살
    "戈": "CUSTOM",    # 🔱 [CUSTOM] 고대 ㄱ자 꺾창
    "矛": "CUSTOM",    # 🗡️ [CUSTOM] 찌르는 장창
    "斤": "1fa93",     # 🪓 도끼
    "斧": "1fa93",     # 🪓 큰 손도끼
    "網": "CUSTOM",    # 🕸️ [CUSTOM] 물고기 잡는 투망 어망
    "鼎": "CUSTOM",    # 🍲 [CUSTOM] 세 발 달린 청동 솥
    "鬲": "CUSTOM",    # 🫕 [CUSTOM] 세 발 달린 토기 솥
    "皿": "1f37d",     # 🍽️ 그릇/접시
    "壺": "1f3fa",     # 🏺 도자기 항아리 병
    "缶": "CUSTOM",    # 🥫 [CUSTOM] 흙으로 빚은 옹기/장군
    "臼": "CUSTOM",    # 🥣 [CUSTOM] 곡식 찧는 절구
    "杵": "CUSTOM",    # 🥢 [CUSTOM] 절구 방망이 공이
    "箕": "CUSTOM",    # 🧺 [CUSTOM] 곡식 까부르는 키
    "帚": "1f9f9",     # 🧹 먼지 쓰는 빗자루
    "卓": "1fa91",     # 🪑 다리 달린 탁자/의자
    "几": "1fa91",     # 🪑 작은 안석 탁자
    "床": "1f6cf",     # 🛏️ 평상/침상
    "繩": "1fa92",     # 🪢 꼬아 만든 밧줄
    "索": "1fa92",     # 🪢 노끈/동아줄
    "針": "1faa1",     # 🪡 바늘과 실
    "鏡": "1fa9e",     # 🪞 비추는 거울
    "鐘": "1f514",     # 🔔 소리 나는 종
    "鼓": "1f941",     # 🥁 둥둥 치는 북
    "磬": "CUSTOM",    # 🎵 [CUSTOM] ㄱ자 옥 경쇠 타악기
    "笛": "1fa88",     # 🪈 피리
    "琴": "CUSTOM",    # 🎹 [CUSTOM] 줄을 얹은 가야금/거문고
    "管": "CUSTOM",    # 🧪 [CUSTOM] 속이 빈 대나무 대롱
    "印": "CUSTOM",    # 📜 [CUSTOM] 붉은 인주 도장/낙관
    "楯": "1f6e1",     # 🛡️ 막아내는 방패

    # 6. 의식주 & 건축 & 문화 (28자)
    "門": "CUSTOM",    # 🚪 [CUSTOM] 대궐식 쌍여닫이 대문
    "戶": "CUSTOM",    # 🚪 [CUSTOM] 한옥 외짝 지게문
    "宮": "1f3ef",     # 🏯 웅장한 궁궐
    "室": "1f3eb",     # 🏫 방
    "堂": "1f3db",     # 🏛️ 큰 전각 대당
    "屋": "1f3e0",     # 🏠 기와집
    "衣": "1f458",     # 👘 옷
    "巾": "1f9e3",     # 🧣 수건/천
    "帶": "1f94b",     # 🥋 허리띠
    "履": "1f45e",     # 👞 신발
    "冠": "1f451",     # 👑 머리에 쓰는 관
    "傘": "2602",      # ☂️ 우산
    "食": "1f371",     # 🍱 음식/밥
    "酒": "1f376",     # 🍶 술병과 잔
    "酉": "1f3fa",     # 🏺 빚은 술 항아리
    "鬯": "CUSTOM",    # 🍷 [CUSTOM] 제사용 울창주 항아리와 국자
    "冊": "1f4d6",     # 📖 펼친 책
    "聿": "1f58c",     # 🖌️ 붓
    "筆": "1f58c",     # 🖌️ 서예 붓
    "墨": "2712",      # ✒️ 진한 먹물
    "紙": "1f4c4",     # 📄 종이
    "硯": "1faa8",     # 🪨 먹을 가는 돌벼루
    "錢": "1fa99",     # 🪙 엽전 동전
    "玉": "1f48e",     # 💎 영롱한 옥/보석
    "瓦": "CUSTOM",    # 🧱 [CUSTOM] 한옥 지붕 기와
    "郭": "1f3ef",     # 🏯 둘러싼 성곽
    "壘": "1f3f0",     # 🏰 군사 보루 요새
}

def run_update():
    out_dir = os.path.join("assets", "svg_drawings")
    os.makedirs(out_dir, exist_ok=True)
    
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
    from hanzi_data import HANZI_DATABASE

    print("🚀 160개 상형한자 직관적 이미지 일러스트 전면 점검 및 갱신 시작...")
    
    updated_count = 0
    custom_count = 0
    emoji_count = 0

    for char, data in HANZI_DATABASE.items():
        clean_char = char.replace("/", "_")
        out_svg = os.path.join(out_dir, f"{clean_char}_drawing.svg")
        
        # 1. 커스텀 전용 직관적 상형 벡터 일러스트 확인
        custom_svg = create_custom_svg(char)
        svg_content = None

        if custom_svg:
            svg_content = custom_svg.strip()
            custom_count += 1
        else:
            # 2. 이모지/오픈모지 벡터 일러스트 다운로드
            code = OPTIMIZED_DRAWING_MAP.get(char, OPTIMIZED_DRAWING_MAP.get(clean_char, "2728"))
            if code != "CUSTOM":
                url_twemoji = f"https://raw.githubusercontent.com/twitter/twemoji/master/assets/svg/{code.lower()}.svg"
                url_openmoji = f"https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/svg/{code.upper()}.svg"
                
                for url in [url_twemoji, url_openmoji]:
                    try:
                        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                        with urllib.request.urlopen(req, timeout=5) as resp:
                            svg_content = resp.read().decode("utf-8")
                            emoji_count += 1
                            break
                    except Exception:
                        continue

        if not svg_content:
            # 폴백 SVG
            svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FEF3C7"/>
  <circle cx="256" cy="256" r="200" fill="#FDE68A" stroke="#F59E0B" stroke-width="16"/>
  <text x="256" y="320" font-size="200" font-family="Arial, sans-serif" font-weight="bold" fill="#D97706" text-anchor="middle">{char}</text>
</svg>"""

        with open(out_svg, "w", encoding="utf-8") as f:
            f.write(svg_content)

        data["drawing_svg"] = svg_content
        updated_count += 1

    print(f"✨ 완료: 총 {updated_count}자 (고유 상형 커스텀 일러스트 {custom_count}자, 고품질 벡터 이모지 {emoji_count}자)")

if __name__ == "__main__":
    run_update()
