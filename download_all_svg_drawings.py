"""
160개 상형한자 최적화 컬러 벡터 일러스트(SVG) 전면 업그레이드 생성기
- 한자의 본래 뜻(상형 기원 및 의미)과 직관적으로 100% 일치하는 고품질 벡터 일러스트 구성
- 직관성이 떨어지는 모든 한자에 대해 고유 맞춤형 커스텀 벡터 일러스트 탑재
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
    custom_assets = {
        # 1) 田 (밭 전): 바둑판 모양의 푸른 논밭/이랑과 벼/작물
        "田": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E8F5E9"/>
  <rect x="56" y="56" width="400" height="400" rx="32" fill="#81C784" stroke="#2E7D32" stroke-width="20"/>
  <line x1="256" y1="56" x2="256" y2="456" stroke="#4E342E" stroke-width="24" stroke-linecap="round"/>
  <line x1="56" y1="256" x2="456" y2="256" stroke="#4E342E" stroke-width="24" stroke-linecap="round"/>
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
  <circle cx="256" cy="256" r="180" fill="none" stroke="#8D6E63" stroke-width="36"/>
  <circle cx="256" cy="256" r="140" fill="#D7CCC8" opacity="0.3"/>
  <circle cx="256" cy="256" r="45" fill="#5D4037" stroke="#3E2723" stroke-width="12"/>
  <circle cx="256" cy="256" r="18" fill="#FFE082"/>
  <line x1="256" y1="76" x2="256" y2="436" stroke="#6D4C41" stroke-width="16"/>
  <line x1="76" y1="256" x2="436" y2="256" stroke="#6D4C41" stroke-width="16"/>
  <line x1="128" y1="128" x2="384" y2="384" stroke="#6D4C41" stroke-width="16"/>
  <line x1="128" y1="384" x2="384" y2="128" stroke="#6D4C41" stroke-width="16"/>
  <rect x="80" y="240" width="352" height="32" rx="8" fill="#4E342E" opacity="0.85"/>
</svg>""",

        # 3) 井 (우물 정): 정자(井)형 돌틀 우물과 맑은 물
        "井": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E0F7FA"/>
  <circle cx="256" cy="256" r="110" fill="#00ACC1"/>
  <circle cx="256" cy="256" r="80" fill="#00838F"/>
  <circle cx="270" cy="240" r="25" fill="#E0F7FA" opacity="0.5"/>
  <rect x="60" y="140" width="392" height="52" rx="12" fill="#8D6E63" stroke="#4E342E" stroke-width="10"/>
  <rect x="60" y="320" width="392" height="52" rx="12" fill="#8D6E63" stroke="#4E342E" stroke-width="10"/>
  <rect x="140" y="60" width="52" height="392" rx="12" fill="#A1887F" stroke="#4E342E" stroke-width="10"/>
  <rect x="320" y="60" width="52" height="392" rx="12" fill="#A1887F" stroke="#4E342E" stroke-width="10"/>
  <line x1="256" y1="60" x2="256" y2="250" stroke="#FFB300" stroke-width="8" stroke-dasharray="8 8"/>
</svg>""",

        # 4) 門 (문 문): 웅장한 대궐식 쌍여닫이 대문
        "門": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF3E0"/>
  <path d="M40 90 L256 50 L472 90 L450 130 L62 130 Z" fill="#D32F2F" stroke="#5D4037" stroke-width="8"/>
  <rect x="64" y="120" width="40" height="330" fill="#8D6E63" stroke="#3E2723" stroke-width="8"/>
  <rect x="408" y="120" width="40" height="330" fill="#8D6E63" stroke="#3E2723" stroke-width="8"/>
  <rect x="110" y="134" width="140" height="310" fill="#B71C1C" stroke="#3E2723" stroke-width="8"/>
  <circle cx="230" cy="280" r="16" fill="#FFD54F" stroke="#FF8F00" stroke-width="4"/>
  <rect x="262" y="134" width="140" height="310" fill="#C62828" stroke="#3E2723" stroke-width="8"/>
  <circle cx="282" cy="280" r="16" fill="#FFD54F" stroke="#FF8F00" stroke-width="4"/>
  <rect x="130" y="160" width="100" height="80" fill="#880E4F" opacity="0.4"/>
  <rect x="282" y="160" width="100" height="80" fill="#880E4F" opacity="0.4"/>
</svg>""",

        # 5) 戶 (지게문 호): 아늑한 한옥 외짝 방문
        "戶": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FAFAFA"/>
  <rect x="100" y="60" width="312" height="392" rx="16" fill="#D7CCC8" stroke="#5D4037" stroke-width="16"/>
  <rect x="124" y="84" width="264" height="344" fill="#FFF9C4" stroke="#8D6E63" stroke-width="10"/>
  <line x1="124" y1="200" x2="388" y2="200" stroke="#8D6E63" stroke-width="8"/>
  <line x1="124" y1="300" x2="388" y2="300" stroke="#8D6E63" stroke-width="8"/>
  <line x1="210" y1="84" x2="210" y2="428" stroke="#8D6E63" stroke-width="8"/>
  <line x1="300" y1="84" x2="300" y2="428" stroke="#8D6E63" stroke-width="8"/>
  <circle cx="160" cy="256" r="18" fill="#FFB300" stroke="#E65100" stroke-width="4"/>
  <path d="M160 270 L160 305" stroke="#E65100" stroke-width="8" stroke-linecap="round"/>
</svg>""",

        # 6) 鶴 (학 학): 붉은 정수리(단정학)와 우아한 자태의 백학/두루미
        "鶴": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E0F7FA"/>
  <!-- 긴 검은 다리 -->
  <line x1="220" y1="340" x2="210" y2="460" stroke="#263238" stroke-width="10" stroke-linecap="round"/>
  <line x1="260" y1="340" x2="275" y2="460" stroke="#263238" stroke-width="10" stroke-linecap="round"/>
  <!-- 백학 몸통과 검은 날개 깃털 -->
  <ellipse cx="240" cy="300" rx="90" ry="60" fill="#ECEFF1" stroke="#CFD8DC" stroke-width="6"/>
  <path d="M210 280 Q290 320 330 350 Q280 370 200 330 Z" fill="#263238"/>
  <!-- 우아한 S자 긴 목 -->
  <path d="M200 280 C180 200 240 160 220 100" fill="none" stroke="#ECEFF1" stroke-width="28" stroke-linecap="round"/>
  <path d="M200 280 C180 200 240 160 220 100" fill="none" stroke="#263238" stroke-width="6"/>
  <!-- 머리와 붉은 정수리(단정) -->
  <circle cx="215" cy="90" r="22" fill="#ECEFF1"/>
  <circle cx="210" cy="74" r="10" fill="#D32F2F"/>
  <!-- 뾰족한 노란 부리와 눈 -->
  <polygon points="195,88 130,95 195,102" fill="#FFA000" stroke="#FF8F00" stroke-width="2"/>
  <circle cx="205" cy="88" r="4" fill="#263238"/>
</svg>""",

        # 7) 爪 (손톱/발톱 조): 맹수의 날카로운 3개의 갈퀴 발톱
        "爪": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF3E0"/>
  <!-- 맹수의 발바닥 뼈대 -->
  <path d="M140 100 L372 100 L340 220 L172 220 Z" fill="#8D6E63" stroke="#4E342E" stroke-width="14"/>
  <!-- 3개의 뾰족하게 굽은 날카로운 맹수 발톱 -->
  <!-- 1번 발톱 (좌) -->
  <path d="M160 220 Q120 340 80 420 Q160 380 200 220 Z" fill="#ECEFF1" stroke="#37474F" stroke-width="12"/>
  <path d="M160 220 Q130 320 90 400" fill="none" stroke="#B0BEC5" stroke-width="6"/>
  <!-- 2번 중앙 큰 발톱 -->
  <path d="M230 220 Q240 370 256 450 Q280 370 290 220 Z" fill="#ECEFF1" stroke="#37474F" stroke-width="12"/>
  <line x1="256" y1="220" x2="256" y2="430" stroke="#B0BEC5" stroke-width="6"/>
  <!-- 3번 발톱 (우) -->
  <path d="M320 220 Q360 340 432 420 Q352 380 312 220 Z" fill="#ECEFF1" stroke="#37474F" stroke-width="12"/>
  <path d="M320 220 Q350 320 422 400" fill="none" stroke="#B0BEC5" stroke-width="6"/>
</svg>""",

        # 8) 臣 (신하 신): 임금 앞에 홀(笏)을 들고 공손히 고개 숙인 신하
        "臣": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#EDE7F6"/>
  <!-- 관모(사모) -->
  <path d="M190 70 L322 70 L340 140 L172 140 Z" fill="#212121"/>
  <rect x="140" y="110" width="232" height="24" rx="8" fill="#424242"/>
  <ellipse cx="256" cy="140" rx="45" ry="15" fill="#37474F"/>
  <!-- 공손히 숙인 얼굴 & 눈 내리깐 신하의 눈(상형 기원) -->
  <circle cx="256" cy="180" r="45" fill="#FFCC80"/>
  <ellipse cx="240" cy="180" rx="14" ry="8" fill="#3E2723"/>
  <ellipse cx="240" cy="182" rx="6" ry="4" fill="#FFFFFF"/>
  <!-- 관복(푸른 공복) -->
  <path d="M150 220 L362 220 L400 450 L112 450 Z" fill="#1565C0" stroke="#0D47A1" stroke-width="12"/>
  <!-- 가슴 흉배 -->
  <rect x="206" y="250" width="100" height="90" rx="8" fill="#D32F2F" stroke="#FFD54F" stroke-width="6"/>
  <circle cx="256" cy="295" r="24" fill="#FFD54F"/>
  <!-- 손에 든 신하의 홀(笏, 옥패) -->
  <rect x="240" y="210" width="32" height="150" rx="6" fill="#E0F2F1" stroke="#004D40" stroke-width="8"/>
</svg>""",

        # 9) 土 (흙 토): 비옥한 땅 위로 도톰하게 솟아오른 흙덩이와 지층
        "土": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF8E1"/>
  <!-- 깊은 지하 지층 -->
  <rect x="40" y="340" width="432" height="110" rx="16" fill="#5D4037" stroke="#3E2723" stroke-width="12"/>
  <rect x="40" y="270" width="432" height="80" fill="#795548"/>
  <line x1="40" y1="270" x2="472" y2="270" stroke="#3E2723" stroke-width="16"/>
  <!-- 땅 위로 도톰하게 솟아오른 기름진 흙더미 (土 상형) -->
  <path d="M140 270 Q256 80 372 270 Z" fill="#8D6E63" stroke="#4E342E" stroke-width="14"/>
  <path d="M190 270 Q256 140 322 270 Z" fill="#A1887F"/>
  <!-- 지층 속 자갈과 양분 -->
  <circle cx="120" cy="380" r="16" fill="#BCAAA4"/>
  <circle cx="256" cy="390" r="20" fill="#BCAAA4"/>
  <circle cx="380" cy="370" r="14" fill="#BCAAA4"/>
</svg>""",

        # 10) 墨 (먹 묵): 황금 용 무늬가 새겨진 검은 먹(墨)과 먹물 번짐
        "墨": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#F5F5F5"/>
  <!-- 화선지 위 짙은 수묵 먹물 번짐 -->
  <circle cx="256" cy="320" r="140" fill="#212121" opacity="0.15"/>
  <circle cx="256" cy="320" r="100" fill="#212121" opacity="0.4"/>
  <circle cx="256" cy="320" r="60" fill="#111111"/>
  <!-- 단단하고 각진 명품 송연묵(먹봉) -->
  <rect x="180" y="70" width="152" height="300" rx="16" fill="#1A1A1A" stroke="#000000" stroke-width="12"/>
  <!-- 먹에 새겨진 황금빛 서체 각인 -->
  <rect x="210" y="110" width="92" height="150" rx="8" fill="none" stroke="#FFD54F" stroke-width="6"/>
  <line x1="256" y1="130" x2="256" y2="240" stroke="#FFD54F" stroke-width="8" stroke-linecap="round"/>
  <circle cx="256" cy="200" r="14" fill="#FFB300"/>
  <!-- 먹 아래 금박 장식 -->
  <rect x="200" y="310" width="112" height="24" rx="4" fill="#FFC107"/>
</svg>""",

        # 11) 硯 (벼루 연): 먹물이 담긴 오목한 석조 벼루와 붓
        "硯": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#ECEFF1"/>
  <!-- 석조 벼루 몸체 (타원/직사각 명품 벼루) -->
  <rect x="70" y="70" width="372" height="372" rx="48" fill="#37474F" stroke="#212121" stroke-width="16"/>
  <rect x="100" y="100" width="312" height="312" rx="32" fill="#455A64"/>
  <!-- 벼루 연당(먹 가는 평평한 곳) & 연지(오목한 먹물 웅덩이) -->
  <rect x="130" y="200" width="252" height="180" rx="16" fill="#263238"/>
  <ellipse cx="256" cy="150" rx="100" ry="36" fill="#111111" stroke="#212121" stroke-width="8"/>
  <ellipse cx="256" cy="152" rx="80" ry="24" fill="#000000"/>
  <circle cx="280" cy="146" r="12" fill="#FFFFFF" opacity="0.3"/>
  <!-- 벼루 위에 걸쳐진 붓 -->
  <line x1="70" y1="430" x2="430" y2="100" stroke="#8D6E63" stroke-width="16" stroke-linecap="round"/>
  <polygon points="70,430 110,390 85,445" fill="#111111"/>
</svg>""",

        # 12) 冊 (책 책): 끈으로 엮은 고대 대나무 죽간(竹簡) 책
        "冊": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF8E1"/>
  <!-- 5개의 나란한 대나무 죽간 살 (冊 상형 형태 100% 일치) -->
  <rect x="90" y="60" width="45" height="392" rx="10" fill="#FFE082" stroke="#FF8F00" stroke-width="8"/>
  <rect x="160" y="60" width="45" height="392" rx="10" fill="#FFE082" stroke="#FF8F00" stroke-width="8"/>
  <rect x="233" y="60" width="45" height="392" rx="10" fill="#FFE082" stroke="#FF8F00" stroke-width="8"/>
  <rect x="306" y="60" width="45" height="392" rx="10" fill="#FFE082" stroke="#FF8F00" stroke-width="8"/>
  <rect x="376" y="60" width="45" height="392" rx="10" fill="#FFE082" stroke="#FF8F00" stroke-width="8"/>
  <!-- 죽간 글씨 먹선 -->
  <line x1="112" y1="120" x2="112" y2="380" stroke="#5D4037" stroke-width="6" stroke-dasharray="16 16"/>
  <line x1="182" y1="120" x2="182" y2="380" stroke="#5D4037" stroke-width="6" stroke-dasharray="16 16"/>
  <line x1="256" y1="120" x2="256" y2="380" stroke="#5D4037" stroke-width="6" stroke-dasharray="16 16"/>
  <line x1="328" y1="120" x2="328" y2="380" stroke="#5D4037" stroke-width="6" stroke-dasharray="16 16"/>
  <line x1="398" y1="120" x2="398" y2="380" stroke="#5D4037" stroke-width="6" stroke-dasharray="16 16"/>
  <!-- 상하로 관통하여 묶은 붉은 가죽 끈 (冊의 가로선) -->
  <line x1="60" y1="170" x2="452" y2="170" stroke="#D32F2F" stroke-width="16" stroke-linecap="round"/>
  <line x1="60" y1="340" x2="452" y2="340" stroke="#D32F2F" stroke-width="16" stroke-linecap="round"/>
</svg>""",

        # 13) 矢 (화살 시): 깃과 청동 화살촉이 달린 날아가는 화살
        "矢": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E1F5FE"/>
  <!-- 바람 가르는 궤적 -->
  <line x1="60" y1="450" x2="180" y2="330" stroke="#81D4FA" stroke-width="8" stroke-dasharray="12 12"/>
  <!-- 곧은 나무 화살대 -->
  <line x1="100" y1="412" x2="390" y2="122" stroke="#6D4C41" stroke-width="18" stroke-linecap="round"/>
  <!-- 날카로운 청동 화살촉(矢 상형 머리) -->
  <polygon points="460,52 360,100 412,152" fill="#78909C" stroke="#263238" stroke-width="10"/>
  <line x1="460" y1="52" x2="386" y2="126" stroke="#ECEFF1" stroke-width="6"/>
  <!-- 화살 꼬리 깃털(羽) -->
  <polygon points="120,392 60,412 100,452 140,412" fill="#D32F2F"/>
  <polygon points="160,352 100,372 120,412 160,372" fill="#D32F2F"/>
</svg>""",

        # 14) 竹 (대나무 죽): 마디가 뚜렷한 푸른 대나무 줄기와 잎
        "竹": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#F1F8E9"/>
  <!-- 좌측 대나무 줄기 -->
  <rect x="140" y="50" width="40" height="412" rx="10" fill="#7CB342" stroke="#33691E" stroke-width="10"/>
  <line x1="130" y1="180" x2="190" y2="180" stroke="#33691E" stroke-width="12" stroke-linecap="round"/>
  <line x1="130" y1="310" x2="190" y2="310" stroke="#33691E" stroke-width="12" stroke-linecap="round"/>
  <!-- 우측 대나무 줄기 -->
  <rect x="330" y="50" width="40" height="412" rx="10" fill="#7CB342" stroke="#33691E" stroke-width="10"/>
  <line x1="320" y1="150" x2="380" y2="150" stroke="#33691E" stroke-width="12" stroke-linecap="round"/>
  <line x1="320" y1="280" x2="380" y2="280" stroke="#33691E" stroke-width="12" stroke-linecap="round"/>
  <!-- V자형 댓잎 클러스터 (竹 상형 부수 형상) -->
  <path d="M140 180 Q80 200 40 250 Q100 230 140 180 Z" fill="#558B2F"/>
  <path d="M140 180 Q100 240 70 300 Q120 250 140 180 Z" fill="#689F38"/>
  <path d="M330 150 Q270 170 230 220 Q290 200 330 150 Z" fill="#558B2F"/>
  <path d="M370 150 Q430 170 470 220 Q410 200 370 150 Z" fill="#558B2F"/>
  <path d="M370 280 Q430 300 460 350 Q410 330 370 280 Z" fill="#689F38"/>
</svg>""",

        # 15) 皿 (그릇 명): 오목하고 정갈한 전통 도자기 그릇/대접
        "皿": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FAFAFA"/>
  <!-- 넓고 오목한 그릇 입구 (타원) -->
  <ellipse cx="256" cy="180" rx="180" ry="60" fill="#E0F2F1" stroke="#00796B" stroke-width="16"/>
  <ellipse cx="256" cy="180" rx="150" ry="45" fill="#B2DFDB"/>
  <!-- 그릇 몸통 (皿 글자 형태의 완만한 곡선) -->
  <path d="M76 180 C90 320 160 380 256 380 C352 380 422 320 436 180 Z" fill="#80CBC4" stroke="#00796B" stroke-width="16"/>
  <!-- 그릇 굽 (바닥 받침대) -->
  <rect x="176" y="380" width="160" height="40" rx="10" fill="#00796B" stroke="#004D40" stroke-width="8"/>
  <!-- 청자 은은한 광택선 -->
  <path d="M120 220 Q256 320 392 220" fill="none" stroke="#E0F2F1" stroke-width="8" stroke-linecap="round"/>
</svg>""",

        # 16) 卓 (탁자 탁): 단정한 원목 4각 식탁/탁자
        "卓": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF8E1"/>
  <!-- 뒤쪽 두 다리 -->
  <rect x="120" y="200" width="30" height="230" fill="#6D4C41"/>
  <rect x="362" y="200" width="30" height="230" fill="#6D4C41"/>
  <!-- 탁자 두꺼운 상판 (원목) -->
  <polygon points="256,90 450,150 256,210 62,150" fill="#A1887F" stroke="#4E342E" stroke-width="12"/>
  <polygon points="62,150 256,210 256,240 62,180" fill="#8D6E63" stroke="#4E342E" stroke-width="10"/>
  <polygon points="450,150 256,210 256,240 450,180" fill="#6D4C41" stroke="#4E342E" stroke-width="10"/>
  <!-- 앞쪽 두 다리 -->
  <rect x="80" y="180" width="36" height="270" rx="8" fill="#8D6E63" stroke="#4E342E" stroke-width="10"/>
  <rect x="396" y="180" width="36" height="270" rx="8" fill="#8D6E63" stroke="#4E342E" stroke-width="10"/>
  <!-- 다리 연결 보강목 -->
  <line x1="100" y1="360" x2="410" y2="360" stroke="#5D4037" stroke-width="14"/>
</svg>""",

        # 17) 几 (안석/궤 궤): 기대어 앉는 전통 안석/낮은 팔걸이 탁자
        "几": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#EFEBE9"/>
  <!-- 几(안석)의 부드러운 아치형 상판 -->
  <path d="M100 160 Q256 120 412 160 L412 210 Q256 170 100 210 Z" fill="#8D6E63" stroke="#4E342E" stroke-width="12"/>
  <!-- 좌측 곡선 다리 -->
  <path d="M100 200 C80 300 100 400 60 440 L110 440 C140 380 130 300 140 200 Z" fill="#6D4C41" stroke="#4E342E" stroke-width="10"/>
  <!-- 우측 곡선 다리 -->
  <path d="M412 200 C432 300 412 400 452 440 L402 440 C372 380 382 300 372 200 Z" fill="#6D4C41" stroke="#4E342E" stroke-width="10"/>
  <!-- 편안한 비단 방석 쿠션 장식 -->
  <ellipse cx="256" cy="150" rx="120" ry="24" fill="#D32F2F" stroke="#B71C1C" stroke-width="6"/>
</svg>""",

        # 18) 根 (뿌리 근): 땅속 깊고 넓게 뻗어나간 거대한 나무 뿌리
        "根": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#EFEBE9"/>
  <!-- 지표면 분할선 -->
  <rect x="40" y="160" width="432" height="292" rx="16" fill="#6D4C41"/>
  <line x1="40" y1="160" x2="472" y2="160" stroke="#3E2723" stroke-width="16"/>
  <!-- 지상 나무 밑동 -->
  <path d="M200 60 L312 60 L330 160 L182 160 Z" fill="#8D6E63" stroke="#4E342E" stroke-width="12"/>
  <!-- 지하로 힘차게 뻗은 뿌리 줄기들 (根 상형) -->
  <path d="M220 160 Q180 260 80 350 Q140 310 210 240 Q180 360 120 430" fill="none" stroke="#D7CCC8" stroke-width="20" stroke-linecap="round"/>
  <path d="M292 160 Q332 260 432 350 Q372 310 302 240 Q332 360 392 430" fill="none" stroke="#D7CCC8" stroke-width="20" stroke-linecap="round"/>
  <!-- 중심 곧은 뿌리(직근) -->
  <path d="M256 160 L256 440" stroke="#FFE082" stroke-width="24" stroke-linecap="round"/>
  <line x1="256" y1="280" x2="210" y2="340" stroke="#D7CCC8" stroke-width="12" stroke-linecap="round"/>
  <line x1="256" y1="320" x2="310" y2="380" stroke="#D7CCC8" stroke-width="12" stroke-linecap="round"/>
</svg>""",

        # 19) 枝 (가지 지): 굵은 원목 줄기에서 뻗어나온 잔가지와 새싹 잎
        "枝": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#F1F8E9"/>
  <!-- 좌측 큰 기둥 줄기 -->
  <path d="M60 50 Q100 256 60 462" fill="none" stroke="#5D4037" stroke-width="52" stroke-linecap="round"/>
  <!-- 오른쪽으로 뻗어나가는 튼튼한 나뭇가지 -->
  <path d="M80 280 C180 270 240 210 380 180" fill="none" stroke="#6D4C41" stroke-width="32" stroke-linecap="round"/>
  <!-- 위아래로 갈라지는 잔가지들 -->
  <path d="M240 230 C280 150 360 110 440 90" fill="none" stroke="#795548" stroke-width="20" stroke-linecap="round"/>
  <path d="M320 200 C360 270 410 320 460 350" fill="none" stroke="#795548" stroke-width="16" stroke-linecap="round"/>
  <!-- 가지 끝에 돋아난 싱그러운 나뭇잎들 -->
  <path d="M440 90 Q480 70 470 110 Q430 110 440 90 Z" fill="#4CAF50"/>
  <path d="M380 180 Q430 160 420 200 Q370 200 380 180 Z" fill="#66BB6A"/>
  <path d="M460 350 Q500 340 480 380 Q440 370 460 350 Z" fill="#4CAF50"/>
  <path d="M280 140 Q320 110 300 150 Z" fill="#81C784"/>
</svg>""",

        # 20) 大 (큰 대): 사람이 두 팔과 두 다리를 양옆으로 활짝 벌린 웅장한 모습
        "大": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF8E1"/>
  <!-- 머리 -->
  <circle cx="256" cy="100" r="45" fill="#FFB300" stroke="#FF8F00" stroke-width="8"/>
  <!-- 가로로 활짝 뻗은 두 팔 (大의 가로획 一) -->
  <line x1="60" y1="200" x2="452" y2="200" stroke="#E65100" stroke-width="36" stroke-linecap="round"/>
  <!-- 몸통과 양옆으로 쩍 벌린 튼튼한 두 다리 (大의 삐침과 파임 人) -->
  <line x1="256" y1="140" x2="256" y2="240" stroke="#E65100" stroke-width="36"/>
  <line x1="256" y1="220" x2="110" y2="440" stroke="#E65100" stroke-width="36" stroke-linecap="round"/>
  <line x1="256" y1="220" x2="402" y2="440" stroke="#E65100" stroke-width="36" stroke-linecap="round"/>
  <!-- 거대함/빛남 아우라 링 -->
  <circle cx="256" cy="256" r="210" fill="none" stroke="#FFE082" stroke-width="12" stroke-dasharray="16 16"/>
</svg>""",

        # 21) 川 (내 천): 세 줄기의 푸른 강물이 굽이쳐 흘러가는 모양
        "川": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E0F2F1"/>
  <!-- 좌측 물줄기 (丿 형태) -->
  <path d="M120 60 Q160 256 80 452" fill="none" stroke="#00ACC1" stroke-width="32" stroke-linecap="round"/>
  <path d="M120 60 Q160 256 80 452" fill="none" stroke="#E0F7FA" stroke-width="12" stroke-linecap="round"/>
  <!-- 가운데 곧은 물줄기 (丨 형태) -->
  <line x1="256" y1="70" x2="256" y2="442" stroke="#0097A7" stroke-width="32" stroke-linecap="round"/>
  <line x1="256" y1="70" x2="256" y2="442" stroke="#E0F7FA" stroke-width="12" stroke-linecap="round"/>
  <!-- 우측 긴 물줄기 (丨/亅 형태) -->
  <path d="M392 60 Q352 256 412 452" fill="none" stroke="#00838F" stroke-width="32" stroke-linecap="round"/>
  <path d="M392 60 Q352 256 412 452" fill="none" stroke="#E0F7FA" stroke-width="12" stroke-linecap="round"/>
  <!-- 물방울 스플래시 -->
  <circle cx="180" cy="200" r="14" fill="#4DD0E1"/>
  <circle cx="330" cy="320" r="14" fill="#4DD0E1"/>
</svg>""",

        # 22) 泉 (샘 천): 바위틈에서 맑고 시원한 옹달샘 물이 솟구치는 모습
        "泉": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E0F7FA"/>
  <!-- 바위 틈 웅덩이 -->
  <path d="M80 420 C60 300 120 280 256 280 C392 280 452 300 432 420 Z" fill="#78909C" stroke="#37474F" stroke-width="16"/>
  <!-- 샘물 웅덩이 수면 -->
  <ellipse cx="256" cy="380" rx="140" ry="50" fill="#00B0FF"/>
  <ellipse cx="256" cy="380" rx="100" ry="30" fill="#80D8FF"/>
  <!-- 솟구쳐 오르는 샘물 분출 기둥 (泉 상형 백(白)+수(水)) -->
  <path d="M256 340 Q210 200 230 110 Q256 60 282 110 Q302 200 256 340 Z" fill="#E1F5FE" stroke="#0091EA" stroke-width="12"/>
  <!-- 양옆으로 떨어지는 영롱한 물방울들 -->
  <path d="M230 120 Q160 160 150 250" fill="none" stroke="#40C4FF" stroke-width="10" stroke-linecap="round"/>
  <path d="M282 120 Q352 160 362 250" fill="none" stroke="#40C4FF" stroke-width="10" stroke-linecap="round"/>
  <circle cx="140" cy="270" r="16" fill="#00B0FF"/>
  <circle cx="372" cy="270" r="16" fill="#00B0FF"/>
</svg>""",

        # 23) 玉 (구슬 옥): 실로 꿴 3개의 영롱한 비취 옥구슬과 금빛 술
        "玉": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E8F5E9"/>
  <!-- 꿴 금실 줄 (玉의 세로 기둥) -->
  <line x1="256" y1="40" x2="256" y2="430" stroke="#FFB300" stroke-width="12"/>
  <!-- 상단 옥구슬 -->
  <circle cx="256" cy="110" r="50" fill="#2E7D32" stroke="#1B5E20" stroke-width="8"/>
  <circle cx="240" cy="95" r="16" fill="#81C784"/>
  <!-- 중단 옥구슬 -->
  <circle cx="256" cy="230" r="55" fill="#43A047" stroke="#1B5E20" stroke-width="8"/>
  <circle cx="238" cy="215" r="18" fill="#A5D6A7"/>
  <!-- 하단 옥구슬 -->
  <circle cx="256" cy="350" r="50" fill="#2E7D32" stroke="#1B5E20" stroke-width="8"/>
  <circle cx="240" cy="335" r="16" fill="#81C784"/>
  <!-- 하단 매듭과 붉은 장식 술 -->
  <circle cx="256" cy="425" r="14" fill="#D32F2F"/>
  <path d="M246 440 L240 480 M256 440 L256 485 M266 440 L272 480" stroke="#D32F2F" stroke-width="6"/>
</svg>""",

        # 24) 冠 (갓/면류관 관): 고대 전통 면류관과 갓
        "冠": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF8E1"/>
  <!-- 평천판 (면류관 윗판) -->
  <rect x="60" y="90" width="392" height="36" rx="8" fill="#212121" stroke="#FFD54F" stroke-width="6"/>
  <!-- 앞뒤로 늘어뜨린 오색 옥구슬 줄(류, 旒) -->
  <line x1="90" y1="126" x2="90" y2="240" stroke="#D32F2F" stroke-width="6" stroke-dasharray="8 8"/>
  <line x1="130" y1="126" x2="130" y2="240" stroke="#1976D2" stroke-width="6" stroke-dasharray="8 8"/>
  <line x1="382" y1="126" x2="382" y2="240" stroke="#388E3C" stroke-width="6" stroke-dasharray="8 8"/>
  <line x1="422" y1="126" x2="422" y2="240" stroke="#FFD54F" stroke-width="6" stroke-dasharray="8 8"/>
  <!-- 관 몸체 모자 -->
  <path d="M150 126 L362 126 L390 340 L122 340 Z" fill="#37474F" stroke="#212121" stroke-width="12"/>
  <!-- 황금 용/봉황 관 띠 장식 -->
  <rect x="120" y="270" width="272" height="40" rx="8" fill="#FFC107" stroke="#FFA000" stroke-width="6"/>
  <circle cx="256" cy="290" r="14" fill="#D32F2F"/>
  <!-- 턱에 매는 붉은 관 끈 -->
  <path d="M140 340 C140 450 256 460 256 460 C256 460 372 450 372 340" fill="none" stroke="#C62828" stroke-width="14" stroke-linecap="round"/>
</svg>""",

        # 25) 舟 (배 주): 세로형 고대 나룻배 (舟의 첫 획 굽은 뱃머리, 2개 가로 칸막이, 중심 노)
        "舟": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E0F7FA"/>
  <path d="M60 140 Q100 120 140 140" fill="none" stroke="#4DD0E1" stroke-width="8" stroke-linecap="round"/>
  <path d="M380 160 Q420 140 460 160" fill="none" stroke="#4DD0E1" stroke-width="8" stroke-linecap="round"/>
  <path d="M40 360 Q80 340 120 360" fill="none" stroke="#4DD0E1" stroke-width="8" stroke-linecap="round"/>
  <path d="M370 380 Q410 360 450 380" fill="none" stroke="#4DD0E1" stroke-width="8" stroke-linecap="round"/>
  <path d="M180 80 Q130 180 130 320 Q140 440 190 480" fill="none" stroke="#B2EBF2" stroke-width="12" stroke-linecap="round"/>
  <path d="M332 80 Q382 180 382 320 Q372 440 322 480" fill="none" stroke="#B2EBF2" stroke-width="12" stroke-linecap="round"/>
  <!-- 선체 외곽 (舟의 세로형 길쭉한 나룻배 본체) -->
  <path d="M210 50 C150 120 140 320 160 430 L352 430 C372 320 362 120 302 50 Z" fill="#8D6E63" stroke="#4E342E" stroke-width="16" stroke-linejoin="round"/>
  <path d="M216 76 C170 140 160 310 180 410 L332 410 C352 310 342 140 296 76 Z" fill="#D7CCC8"/>
  <!-- 뱃머리 이물 (舟의 첫 획 '丿' 모양 선두) -->
  <path d="M210 50 Q230 40 280 46 L296 76 Q250 64 216 76 Z" fill="#5D4037"/>
  <path d="M210 50 Q200 70 170 100" fill="none" stroke="#4E342E" stroke-width="12" stroke-linecap="round"/>
  <!-- 배 내부 2개 가로 칸막이 좌석 (舟 내부 두 가로획) -->
  <rect x="166" y="170" width="180" height="28" rx="6" fill="#A1887F" stroke="#4E342E" stroke-width="8"/>
  <circle cx="200" cy="184" r="4" fill="#3E2723"/>
  <circle cx="312" cy="184" r="4" fill="#3E2723"/>
  <rect x="170" y="270" width="172" height="28" rx="6" fill="#A1887F" stroke="#4E342E" stroke-width="8"/>
  <circle cx="204" cy="284" r="4" fill="#3E2723"/>
  <circle cx="308" cy="284" r="4" fill="#3E2723"/>
  <!-- 중심 노와 손잡이 핀 (舟의 가운데 획과 점) -->
  <line x1="256" y1="100" x2="256" y2="440" stroke="#FFB300" stroke-width="12" stroke-linecap="round"/>
  <polygon points="246,420 266,420 260,470 252,470" fill="#FFA000" stroke="#FF8F00" stroke-width="4"/>
  <circle cx="280" cy="225" r="12" fill="#D32F2F" stroke="#B71C1C" stroke-width="4"/>
  <rect x="160" y="420" width="192" height="20" rx="4" fill="#5D4037"/>
</svg>""",

        # 26) 氣 (기운 기): 솟아오르는 구름 김과 소용돌이치는 생명 에너지
        "氣": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#EDE7F6"/>
  <!-- 회오리치며 피어오르는 3단 기운 구름 (氣 상형) -->
  <path d="M120 380 C80 340 140 280 200 300 C240 240 320 250 340 300 C400 280 440 340 390 380 Z" fill="#B39DDB" stroke="#7E57C2" stroke-width="12"/>
  <path d="M160 260 C130 220 180 170 230 190 C260 140 320 150 340 190 C380 170 410 220 380 260 Z" fill="#D1C4E9" stroke="#7E57C2" stroke-width="10"/>
  <path d="M210 160 C190 120 230 80 270 100 C290 60 340 70 350 100 C380 90 400 130 380 160 Z" fill="#EDE7F6" stroke="#5E35B1" stroke-width="10"/>
  <!-- 솟구치는 에너지 광선 -->
  <line x1="256" y1="440" x2="256" y2="390" stroke="#FFB300" stroke-width="12" stroke-linecap="round"/>
  <line x1="160" y1="420" x2="180" y2="380" stroke="#FFB300" stroke-width="10" stroke-linecap="round"/>
  <line x1="352" y1="420" x2="332" y2="380" stroke="#FFB300" stroke-width="10" stroke-linecap="round"/>
</svg>""",

        # 27) 聿 (붓 율): 손으로 붓을 곧게 쥐고 글씨를 쓰는 모습
        "聿": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF9C4"/>
  <!-- 수직으로 곧게 선 대나무 붓대 -->
  <line x1="256" y1="50" x2="256" y2="400" stroke="#8D6E63" stroke-width="24" stroke-linecap="round"/>
  <!-- 붓을 쥔 사람 손가락들 (聿 상형) -->
  <path d="M150 180 Q256 160 270 180" fill="none" stroke="#FFB74D" stroke-width="28" stroke-linecap="round"/>
  <path d="M140 240 Q256 220 280 240" fill="none" stroke="#FFB74D" stroke-width="28" stroke-linecap="round"/>
  <path d="M150 300 Q256 280 270 300" fill="none" stroke="#FFB74D" stroke-width="28" stroke-linecap="round"/>
  <!-- 붓 촉(모필)과 먹물 한 점 -->
  <polygon points="238,400 274,400 256,465" fill="#1A1A1A"/>
  <circle cx="256" cy="480" r="10" fill="#1A1A1A"/>
</svg>""",

        # 28) 豆 (콩 두): 꼬투리가 벌어져 통통한 콩알 3개가 드러난 모양
        "豆": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#F1F8E9"/>
  <!-- 둥글게 휜 녹색 콩깍지 꼬투리 -->
  <path d="M80 340 C140 180 372 180 432 340 C360 260 152 260 80 340 Z" fill="#81C784" stroke="#2E7D32" stroke-width="14"/>
  <!-- 꼬투리 속 3개의 영롱한 콩알 (豆 상형) -->
  <circle cx="170" cy="270" r="36" fill="#4CAF50" stroke="#1B5E20" stroke-width="8"/>
  <circle cx="160" cy="260" r="10" fill="#A5D6A7"/>
  <circle cx="256" cy="250" r="40" fill="#4CAF50" stroke="#1B5E20" stroke-width="8"/>
  <circle cx="245" cy="240" r="12" fill="#A5D6A7"/>
  <circle cx="342" cy="270" r="36" fill="#4CAF50" stroke="#1B5E20" stroke-width="8"/>
  <circle cx="330" cy="260" r="10" fill="#A5D6A7"/>
  <!-- 꼬투리 꼭지 줄기 -->
  <path d="M80 340 Q50 350 40 370" fill="none" stroke="#2E7D32" stroke-width="12" stroke-linecap="round"/>
</svg>""",

        # 29) 米 (쌀 미): 탈곡되어 사방으로 고르게 흩어진 통통한 쌀알들
        "米": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFFDE7"/>
  <!-- 중앙 교차선 (米의 十자 중심) -->
  <line x1="256" y1="80" x2="256" y2="432" stroke="#FFA000" stroke-width="12" stroke-linecap="round"/>
  <line x1="80" y1="256" x2="432" y2="256" stroke="#FFA000" stroke-width="12" stroke-linecap="round"/>
  <!-- 4방향 흩어진 낟알들 (米의 八, 丷 형태 쌀알) -->
  <ellipse cx="160" cy="160" rx="36" ry="20" transform="rotate(-45 160 160)" fill="#FFFFFF" stroke="#FFB300" stroke-width="8"/>
  <ellipse cx="352" cy="160" rx="36" ry="20" transform="rotate(45 352 160)" fill="#FFFFFF" stroke="#FFB300" stroke-width="8"/>
  <ellipse cx="160" cy="352" rx="36" ry="20" transform="rotate(45 160 352)" fill="#FFFFFF" stroke="#FFB300" stroke-width="8"/>
  <ellipse cx="352" cy="352" rx="36" ry="20" transform="rotate(-45 352 352)" fill="#FFFFFF" stroke="#FFB300" stroke-width="8"/>
  <!-- 중앙 황금 벼 낟알 -->
  <circle cx="256" cy="256" r="28" fill="#FFD54F" stroke="#FF8F00" stroke-width="8"/>
</svg>""",

        # 30) 麥 (보리 맥): 수염(까끄라기)이 길게 자란 황금빛 보리 이삭
        "麥": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFFDE7"/>
  <!-- 줄기 -->
  <line x1="256" y1="180" x2="256" y2="460" stroke="#8D6E63" stroke-width="16" stroke-linecap="round"/>
  <!-- 좌우 보리 낱알들과 긴 까끄라기 수염들 -->
  <!-- 1단 -->
  <ellipse cx="220" cy="220" rx="32" ry="18" transform="rotate(-30 220 220)" fill="#FFE082" stroke="#FFA000" stroke-width="6"/>
  <line x1="200" y1="210" x2="80" y2="120" stroke="#FF8F00" stroke-width="8" stroke-linecap="round"/>
  <ellipse cx="292" cy="220" rx="32" ry="18" transform="rotate(30 292 220)" fill="#FFE082" stroke="#FFA000" stroke-width="6"/>
  <line x1="312" y1="210" x2="432" y2="120" stroke="#FF8F00" stroke-width="8" stroke-linecap="round"/>
  <!-- 2단 -->
  <ellipse cx="220" cy="290" rx="32" ry="18" transform="rotate(-30 220 290)" fill="#FFD54F" stroke="#FFA000" stroke-width="6"/>
  <line x1="200" y1="280" x2="70" y2="190" stroke="#FF8F00" stroke-width="8" stroke-linecap="round"/>
  <ellipse cx="292" cy="290" rx="32" ry="18" transform="rotate(30 292 290)" fill="#FFD54F" stroke="#FFA000" stroke-width="6"/>
  <line x1="312" y1="280" x2="442" y2="190" stroke="#FF8F00" stroke-width="8" stroke-linecap="round"/>
  <!-- 꼭대기 보리 낟알과 긴 수염 -->
  <ellipse cx="256" cy="150" rx="22" ry="34" fill="#FFE082" stroke="#FFA000" stroke-width="6"/>
  <line x1="256" y1="120" x2="256" y2="40" stroke="#FF8F00" stroke-width="10" stroke-linecap="round"/>
</svg>""",

        # 31) 苗 (모 묘): 물 찬 논(田)에 가지런히 심은 어린 벼 모(苗)
        "苗": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E8F5E9"/>
  <!-- 찰랑이는 논물 바닥 (田) -->
  <rect x="56" y="280" width="400" height="176" rx="24" fill="#81D4FA" stroke="#0288D1" stroke-width="14"/>
  <line x1="256" y1="280" x2="256" y2="456" stroke="#0288D1" stroke-width="10"/>
  <!-- 3포기의 파릇파릇한 어린 볏모 (苗 상형) -->
  <!-- 좌측 모 -->
  <path d="M140 320 Q100 220 80 180 Q130 220 140 320 Z" fill="#4CAF50"/>
  <path d="M140 320 Q160 200 180 170 Q160 230 140 320 Z" fill="#66BB6A"/>
  <!-- 중앙 모 (가장 큼) -->
  <path d="M256 310 Q220 170 190 100 Q240 160 256 310 Z" fill="#43A047"/>
  <path d="M256 310 Q280 150 320 90 Q290 160 256 310 Z" fill="#4CAF50"/>
  <line x1="256" y1="310" x2="256" y2="80" stroke="#2E7D32" stroke-width="8"/>
  <!-- 우측 모 -->
  <path d="M372 320 Q340 220 330 180 Q370 220 372 320 Z" fill="#4CAF50"/>
  <path d="M372 320 Q400 200 432 170 Q390 230 372 320 Z" fill="#66BB6A"/>
</svg>""",

        # 32) 圃 (채소밭 포): 울타리를 두르고 이랑에 가꾼 채소 텃밭
        "圃": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E8F8F5"/>
  <!-- 사방 튼튼한 나무 울타리 (囗 상형) -->
  <rect x="56" y="56" width="400" height="400" rx="24" fill="#C8E6C9" stroke="#5D4037" stroke-width="18"/>
  <!-- 밭 이랑 3줄 -->
  <rect x="90" y="100" width="332" height="70" rx="12" fill="#8D6E63"/>
  <rect x="90" y="220" width="332" height="70" rx="12" fill="#8D6E63"/>
  <rect x="90" y="340" width="332" height="70" rx="12" fill="#8D6E63"/>
  <!-- 이랑마다 자라난 싱싱한 배추와 당근 -->
  <circle cx="150" cy="135" r="22" fill="#4CAF50"/>
  <circle cx="256" cy="135" r="22" fill="#4CAF50"/>
  <circle cx="362" cy="135" r="22" fill="#4CAF50"/>
  <circle cx="150" cy="255" r="22" fill="#66BB6A"/>
  <circle cx="256" cy="255" r="22" fill="#66BB6A"/>
  <circle cx="362" cy="255" r="22" fill="#66BB6A"/>
  <circle cx="150" cy="375" r="22" fill="#81C784"/>
  <circle cx="256" cy="375" r="22" fill="#81C784"/>
  <circle cx="362" cy="375" r="22" fill="#81C784"/>
</svg>""",

        # 33) 堂 (대당 당): 높은 석조 축대 위에 위풍당당하게 지은 큰 전각
        "堂": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF3E0"/>
  <!-- 높은 기단/축대 (堂의 土 받침 상형) -->
  <polygon points="40,450 472,450 440,360 72,360" fill="#78909C" stroke="#37474F" stroke-width="12"/>
  <!-- 웅장한 팔작지붕 처마 -->
  <path d="M30 150 Q256 70 482 150 L440 210 Q256 140 72 210 Z" fill="#D32F2F" stroke="#5D4037" stroke-width="12"/>
  <!-- 4개의 굵은 붉은 기둥 -->
  <rect x="100" y="210" width="28" height="150" fill="#C62828" stroke="#3E2723" stroke-width="6"/>
  <rect x="190" y="210" width="28" height="150" fill="#C62828" stroke="#3E2723" stroke-width="6"/>
  <rect x="294" y="210" width="28" height="150" fill="#C62828" stroke="#3E2723" stroke-width="6"/>
  <rect x="384" y="210" width="28" height="150" fill="#C62828" stroke="#3E2723" stroke-width="6"/>
  <!-- 전각 현판 -->
  <rect x="210" y="160" width="92" height="40" rx="4" fill="#212121" stroke="#FFD54F" stroke-width="4"/>
  <circle cx="256" cy="180" r="8" fill="#FFD54F"/>
</svg>""",

        # 34) 郭 (성곽 곽): 도성을 둘러싼 웅장한 돌 성벽과 성문
        "郭": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#ECEFF1"/>
  <!-- 성벽 몸체와 성가퀴(여장, 배틀먼트) -->
  <path d="M50 200 L110 200 L110 230 L170 230 L170 200 L230 200 L230 230 L290 230 L290 200 L350 200 L350 230 L410 230 L410 200 L462 200 L462 450 L50 450 Z" fill="#607D8B" stroke="#263238" stroke-width="14"/>
  <!-- 성벽 석축 돌무늬선 -->
  <line x1="50" y1="280" x2="462" y2="280" stroke="#37474F" stroke-width="8"/>
  <line x1="50" y1="360" x2="462" y2="360" stroke="#37474F" stroke-width="8"/>
  <!-- 웅장한 아치형 무지개 성문(홍예문) -->
  <path d="M190 450 L190 340 Q256 280 322 340 L322 450 Z" fill="#263238" stroke="#FFD54F" stroke-width="8"/>
  <!-- 성루 누각 지붕 -->
  <path d="M120 120 Q256 60 392 120 L370 170 Q256 120 142 170 Z" fill="#D32F2F" stroke="#3E2723" stroke-width="10"/>
</svg>""",

        # 35) 壘 (보루 루): 흙과 돌을 3단으로 견고하게 쌓아올린 군사 요새/보루
        "壘": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#EFEBE9"/>
  <!-- 1단 하부 거대 석축 -->
  <polygon points="40,450 472,450 430,340 82,340" fill="#5D4037" stroke="#3E2723" stroke-width="12"/>
  <!-- 2단 중부 방어 보루 (壘 상형) -->
  <polygon points="90,340 422,340 380,230 132,230" fill="#795548" stroke="#3E2723" stroke-width="10"/>
  <!-- 3단 상부 망루 보루 요새 -->
  <polygon points="150,230 362,230 330,140 182,140" fill="#8D6E63" stroke="#3E2723" stroke-width="10"/>
  <!-- 망루 위 휘날리는 군사 깃발 -->
  <line x1="256" y1="140" x2="256" y2="50" stroke="#212121" stroke-width="10"/>
  <polygon points="256,50 340,80 256,110" fill="#D32F2F"/>
</svg>""",

        # 36) 帶 (띠 대): 화려한 옥/금 장식이 달린 전통 비단 허리띠
        "帶": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFEBEE"/>
  <!-- 허리에 두르는 붉은 비단 띠 (가로) -->
  <rect x="40" y="140" width="432" height="80" rx="16" fill="#C62828" stroke="#B71C1C" stroke-width="12"/>
  <!-- 중앙 황금 옥 띠돈 버클 -->
  <rect x="206" y="120" width="100" height="120" rx="20" fill="#FFD54F" stroke="#FF8F00" stroke-width="10"/>
  <circle cx="256" cy="180" r="22" fill="#00E676" stroke="#00A152" stroke-width="4"/>
  <!-- 아래로 길게 늘어뜨린 장식 띠 자락 2줄 -->
  <rect x="180" y="240" width="60" height="210" rx="10" fill="#D32F2F" stroke="#B71C1C" stroke-width="8"/>
  <rect x="272" y="240" width="60" height="210" rx="10" fill="#D32F2F" stroke="#B71C1C" stroke-width="8"/>
  <!-- 띠 끝 금빛 수술 장식 -->
  <rect x="180" y="420" width="60" height="30" fill="#FFD54F"/>
  <rect x="272" y="420" width="60" height="30" fill="#FFD54F"/>
</svg>""",

        # 37) 巾 (수건 건): 걸이에 단정하게 걸려 늘어뜨려진 고운 천/수건
        "巾": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E1F5FE"/>
  <!-- 수건걸이 나무 가로대 (巾의 윗 가로획) -->
  <rect x="80" y="90" width="352" height="28" rx="8" fill="#8D6E63" stroke="#4E342E" stroke-width="8"/>
  <circle cx="80" cy="104" r="18" fill="#5D4037"/>
  <circle cx="432" cy="104" r="18" fill="#5D4037"/>
  <!-- 걸이에 걸쳐 아래로 드리워진 부드러운 직물 수건 (巾 상형) -->
  <path d="M140 104 L372 104 L350 430 L162 430 Z" fill="#ECEFF1" stroke="#90A4AE" stroke-width="12"/>
  <!-- 수건 중앙 주름선 -->
  <line x1="256" y1="104" x2="256" y2="430" stroke="#CFD8DC" stroke-width="10"/>
  <!-- 하단 단아한 자수 문양 띠 -->
  <rect x="165" y="370" width="182" height="30" fill="#42A5F5"/>
  <circle cx="256" cy="385" r="8" fill="#FFFFFF"/>
</svg>""",

        # 38) 履 (신 리): 코가 우아하게 들린 비단 꽃신(혜, 履)
        "履": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FAFAFA"/>
  <!-- 튼튼한 가죽 신발 바닥창 -->
  <path d="M80 340 C140 370 360 370 432 300 L440 340 C360 410 140 410 80 360 Z" fill="#5D4037"/>
  <!-- 코가 솟아오른 전통 비단 신발 몸체 (履 상형) -->
  <path d="M90 220 C120 220 160 300 240 300 C340 300 390 220 430 200 C450 250 440 330 380 340 C280 360 140 350 90 320 Z" fill="#D32F2F" stroke="#B71C1C" stroke-width="12"/>
  <!-- 신발 목 안감과 금박 당초문 장식 -->
  <ellipse cx="180" cy="240" rx="60" ry="24" fill="#FFEBEE" stroke="#FFD54F" stroke-width="6"/>
  <path d="M300 280 Q360 270 410 240" fill="none" stroke="#FFD54F" stroke-width="8" stroke-linecap="round"/>
  <circle cx="410" cy="230" r="10" fill="#FFD54F"/>
</svg>""",

        # 39) 尾 (꼬리 미): 탐스럽게 둥글게 말려 올라간 털북숭이 꼬리
        "尾": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF3E0"/>
  <!-- 동물 엉덩이 실루엣 -->
  <circle cx="120" cy="380" r="80" fill="#E65100"/>
  <!-- 풍성하게 위로 솟구쳐 말린 탐스러운 꼬리 (尾 상형) -->
  <path d="M150 340 C190 200 280 80 400 90 C470 100 450 240 350 300 C270 350 210 390 150 380 Z" fill="#FF9800" stroke="#E65100" stroke-width="14"/>
  <!-- 꼬리 끝 하얗고 부드러운 털 포인트 -->
  <path d="M360 100 C430 110 440 200 380 250 C360 210 350 150 360 100 Z" fill="#FFFFFF"/>
  <!-- 꼬리 결 털 선 -->
  <path d="M220 320 Q290 240 350 230" fill="none" stroke="#FFE0B2" stroke-width="10" stroke-linecap="round"/>
</svg>""",

        # 40) 毛 (털 모): 부드럽고 윤기 나게 굽이치는 3가닥 털
        "毛": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FAFAFA"/>
  <!-- 3줄기의 유려한 털 가닥 (毛 상형 100% 일치) -->
  <path d="M160 80 C120 220 220 340 360 420" fill="none" stroke="#8D6E63" stroke-width="32" stroke-linecap="round"/>
  <path d="M256 120 C220 250 290 340 400 390" fill="none" stroke="#A1887F" stroke-width="26" stroke-linecap="round"/>
  <path d="M120 180 C180 260 220 310 300 350" fill="none" stroke="#BCAAA4" stroke-width="20" stroke-linecap="round"/>
  <!-- 부드러운 솜털 모근 -->
  <ellipse cx="160" cy="80" rx="24" ry="16" fill="#6D4C41"/>
  <ellipse cx="256" cy="120" rx="20" ry="14" fill="#6D4C41"/>
</svg>""",

        # 41) 鼎 (솥 정)
        "鼎": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#ECEFF1"/>
  <path d="M100 130 L100 80 Q100 60 120 60 L140 60 L140 130" fill="none" stroke="#37474F" stroke-width="20"/>
  <path d="M412 130 L412 80 Q412 60 392 60 L372 60 L372 130" fill="none" stroke="#37474F" stroke-width="20"/>
  <path d="M90 130 Q90 320 256 330 Q422 320 422 130 Z" fill="#546E7A" stroke="#263238" stroke-width="16"/>
  <rect x="100" y="160" width="312" height="40" rx="8" fill="#78909C"/>
  <circle cx="160" cy="180" r="10" fill="#CFD8DC"/>
  <circle cx="256" cy="180" r="10" fill="#CFD8DC"/>
  <circle cx="352" cy="180" r="10" fill="#CFD8DC"/>
  <path d="M130 310 L100 450" stroke="#37474F" stroke-width="32" stroke-linecap="round"/>
  <path d="M256 325 L256 460" stroke="#263238" stroke-width="34" stroke-linecap="round"/>
  <path d="M382 310 L412 450" stroke="#37474F" stroke-width="32" stroke-linecap="round"/>
</svg>""",

        # 42) 戈 (창 과)
        "戈": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FBE9E7"/>
  <line x1="80" y1="440" x2="380" y2="100" stroke="#5D4037" stroke-width="22" stroke-linecap="round"/>
  <path d="M350 130 L450 70 L430 160 L380 180 Z" fill="#78909C" stroke="#263238" stroke-width="10"/>
  <path d="M330 150 L270 230 L310 240 Z" fill="#90A4AE" stroke="#263238" stroke-width="8"/>
  <circle cx="350" cy="140" r="18" fill="#D32F2F"/>
  <path d="M350 140 Q330 190 320 220" stroke="#D32F2F" stroke-width="8" stroke-linecap="round"/>
</svg>""",

        # 43) 矛 (창 모)
        "矛": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#ECEFF1"/>
  <line x1="90" y1="422" x2="360" y2="152" stroke="#4E342E" stroke-width="20" stroke-linecap="round"/>
  <path d="M340 170 Q430 100 460 52 Q412 142 362 192 Z" fill="#B0BEC5" stroke="#263238" stroke-width="10"/>
  <line x1="350" y1="180" x2="455" y2="57" stroke="#ECEFF1" stroke-width="6"/>
  <path d="M330 180 Q310 240 280 260 Q320 230 350 200 Z" fill="#C62828"/>
</svg>""",

        # 44) 印 (도장 인)
        "印": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFEBEE"/>
  <path d="M180 80 L332 80 L360 260 L152 260 Z" fill="#D7CCC8" stroke="#5D4037" stroke-width="14"/>
  <ellipse cx="256" cy="80" rx="76" ry="30" fill="#BCAAA4" stroke="#5D4037" stroke-width="12"/>
  <rect x="140" y="260" width="232" height="40" rx="8" fill="#D32F2F" stroke="#B71C1C" stroke-width="8"/>
  <rect x="176" y="340" width="160" height="120" rx="16" fill="none" stroke="#C62828" stroke-width="16"/>
  <path d="M210 370 L240 430 M240 370 L210 430 M280 370 L280 430 M265 400 L305 400" stroke="#C62828" stroke-width="12" stroke-linecap="round"/>
</svg>""",

        # 45) 網 (그물 망)
        "網": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E1F5FE"/>
  <path d="M80 120 Q256 60 432 120 Q410 420 256 450 Q102 420 80 120 Z" fill="#81D4FA" opacity="0.3" stroke="#0277BD" stroke-width="14"/>
  <path d="M120 110 L390 380 M180 90 L420 330 M260 80 L430 250 M85 180 L330 430 M95 270 L250 445" stroke="#01579B" stroke-width="8"/>
  <path d="M390 110 L120 380 M330 90 L90 330 M250 80 L80 250 M425 180 L180 430 M415 270 L260 445" stroke="#01579B" stroke-width="8"/>
  <circle cx="100" cy="380" r="14" fill="#455A64"/>
  <circle cx="170" cy="425" r="14" fill="#455A64"/>
  <circle cx="256" cy="450" r="14" fill="#455A64"/>
  <circle cx="342" cy="425" r="14" fill="#455A64"/>
  <circle cx="412" cy="380" r="14" fill="#455A64"/>
</svg>""",

        # 46) 缶 (장군/항아리 부)
        "缶": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#EFEBE9"/>
  <ellipse cx="256" cy="110" rx="90" ry="24" fill="#8D6E63" stroke="#4E342E" stroke-width="12"/>
  <ellipse cx="256" cy="110" rx="60" ry="14" fill="#3E2723"/>
  <path d="M170 120 C100 180 80 280 120 380 C140 430 200 450 256 450 C312 450 372 430 392 380 C432 280 412 180 342 120 Z" fill="#6D4C41" stroke="#3E2723" stroke-width="16"/>
  <path d="M120 280 Q256 340 392 280" fill="none" stroke="#A1887F" stroke-width="12" stroke-linecap="round"/>
  <path d="M140 240 Q256 300 372 240" fill="none" stroke="#D7CCC8" stroke-width="8" stroke-dasharray="12 12"/>
</svg>""",

        # 47) 瓦 (기와 와)
        "瓦": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#ECEFF1"/>
  <path d="M80 360 C80 260 160 260 160 360 L140 440 L60 440 Z" fill="#546E7A" stroke="#263238" stroke-width="10"/>
  <path d="M216 360 C216 260 296 260 296 360 L276 440 L196 440 Z" fill="#546E7A" stroke="#263238" stroke-width="10"/>
  <path d="M352 360 C352 260 432 260 432 360 L412 440 L332 440 Z" fill="#546E7A" stroke="#263238" stroke-width="10"/>
  <ellipse cx="120" cy="270" rx="42" ry="24" fill="#78909C" stroke="#263238" stroke-width="8"/>
  <ellipse cx="256" cy="270" rx="42" ry="24" fill="#78909C" stroke="#263238" stroke-width="8"/>
  <ellipse cx="392" cy="270" rx="42" ry="24" fill="#78909C" stroke="#263238" stroke-width="8"/>
  <circle cx="256" cy="270" r="12" fill="#CFD8DC"/>
  <path d="M40 220 Q256 160 472 220 L450 170 Q256 120 62 170 Z" fill="#37474F" stroke="#212121" stroke-width="10"/>
</svg>""",

        # 48) 管 (대롱 관)
        "管": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#F1F8E9"/>
  <rect x="180" y="50" width="152" height="412" rx="20" fill="#8BC34A" stroke="#33691E" stroke-width="14"/>
  <ellipse cx="256" cy="70" rx="56" ry="20" fill="#558B2F" stroke="#33691E" stroke-width="8"/>
  <ellipse cx="256" cy="70" rx="36" ry="12" fill="#1B5E20"/>
  <rect x="164" y="160" width="184" height="24" rx="10" fill="#689F38" stroke="#33691E" stroke-width="8"/>
  <rect x="164" y="280" width="184" height="24" rx="10" fill="#689F38" stroke="#33691E" stroke-width="8"/>
  <rect x="164" y="400" width="184" height="24" rx="10" fill="#689F38" stroke="#33691E" stroke-width="8"/>
  <path d="M340 170 Q420 140 440 180 Q390 190 340 175 Z" fill="#4CAF50"/>
</svg>""",

        # 49) 琴 (거문고/가야금 금)
        "琴": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFFDE7"/>
  <rect x="120" y="50" width="272" height="412" rx="30" fill="#8D6E63" stroke="#4E342E" stroke-width="16"/>
  <ellipse cx="256" cy="256" rx="32" ry="16" fill="#3E2723"/>
  <line x1="160" y1="60" x2="160" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="192" y1="60" x2="192" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="224" y1="60" x2="224" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="256" y1="60" x2="256" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="288" y1="60" x2="288" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="320" y1="60" x2="320" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <line x1="352" y1="60" x2="352" y2="450" stroke="#FFF9C4" stroke-width="6"/>
  <path d="M150 160 L170 170 L150 180 Z" fill="#FFE082"/>
  <path d="M182 200 L202 210 L182 220 Z" fill="#FFE082"/>
  <path d="M214 240 L234 250 L214 260 Z" fill="#FFE082"/>
  <path d="M246 280 L266 290 L246 300 Z" fill="#FFE082"/>
  <path d="M278 320 L298 330 L278 340 Z" fill="#FFE082"/>
  <path d="M310 360 L330 370 L310 380 Z" fill="#FFE082"/>
  <path d="M342 400 L362 410 L342 420 Z" fill="#FFE082"/>
</svg>""",

        # 50) 磬 (경쇠 경)
        "磬": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#F3E5F5"/>
  <rect x="80" y="50" width="352" height="30" rx="8" fill="#5D4037" stroke="#3E2723" stroke-width="8"/>
  <rect x="100" y="70" width="24" height="390" fill="#5D4037"/>
  <rect x="388" y="70" width="24" height="390" fill="#5D4037"/>
  <line x1="200" y1="80" x2="200" y2="160" stroke="#D32F2F" stroke-width="8"/>
  <line x1="312" y1="80" x2="312" y2="160" stroke="#D32F2F" stroke-width="8"/>
  <path d="M140 200 L256 160 L372 260 L340 320 L256 240 L160 270 Z" fill="#80CBC4" stroke="#004D40" stroke-width="14"/>
  <line x1="320" y1="360" x2="420" y2="280" stroke="#FFB300" stroke-width="12" stroke-linecap="round"/>
  <circle cx="320" cy="360" r="20" fill="#D32F2F"/>
</svg>""",

        # 51) 森 (나무빽빽할 삼)
        "森": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E8F5E9"/>
  <rect x="242" y="160" width="28" height="90" fill="#795548"/>
  <circle cx="256" cy="130" r="65" fill="#2E7D32"/>
  <circle cx="230" cy="120" r="45" fill="#43A047"/>
  <rect x="142" y="340" width="28" height="100" fill="#795548"/>
  <circle cx="156" cy="300" r="75" fill="#1B5E20"/>
  <circle cx="130" cy="280" r="55" fill="#388E3C"/>
  <rect x="342" y="340" width="28" height="100" fill="#795548"/>
  <circle cx="356" cy="300" r="75" fill="#2E7D32"/>
  <circle cx="380" cy="280" r="55" fill="#4CAF50"/>
</svg>""",

        # 52) 林 (수풀 림)
        "林": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E8F8F5"/>
  <rect x="156" y="270" width="32" height="160" fill="#6D4C41"/>
  <circle cx="172" cy="210" r="95" fill="#2E7D32"/>
  <circle cx="145" cy="185" r="70" fill="#43A047"/>
  <rect x="324" y="270" width="32" height="160" fill="#6D4C41"/>
  <circle cx="340" cy="210" r="95" fill="#388E3C"/>
  <circle cx="365" cy="185" r="70" fill="#66BB6A"/>
</svg>""",

        # 53) 臼 (절구 구) & 杵 (공이 처)
        "臼": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFFDE7"/>
  <path d="M120 120 L392 120 C360 240 380 360 400 440 L112 440 C132 360 152 240 120 120 Z" fill="#8D6E63" stroke="#4E342E" stroke-width="16"/>
  <ellipse cx="256" cy="140" rx="120" ry="40" fill="#D7CCC8" stroke="#4E342E" stroke-width="10"/>
  <ellipse cx="256" cy="140" rx="90" ry="25" fill="#5D4037"/>
  <circle cx="240" cy="140" r="8" fill="#FFFFFF"/>
  <circle cx="265" cy="142" r="7" fill="#FFFFFF"/>
  <circle cx="252" cy="135" r="6" fill="#FFFFFF"/>
</svg>""",

        "杵": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFFDE7"/>
  <path d="M226 60 L286 60 Q270 200 266 256 Q270 312 286 452 L226 452 Q242 312 246 256 Q242 200 226 60 Z" fill="#A1887F" stroke="#4E342E" stroke-width="14"/>
  <ellipse cx="256" cy="70" rx="30" ry="10" fill="#6D4C41"/>
  <ellipse cx="256" cy="442" rx="30" ry="10" fill="#6D4C41"/>
</svg>""",

        # 54) 箕 (키 기)
        "箕": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF9C4"/>
  <path d="M100 100 L412 100 L370 420 L142 420 Z" fill="#FFE082" stroke="#FF8F00" stroke-width="16"/>
  <path d="M100 100 Q256 60 412 100 L400 140 Q256 100 112 140 Z" fill="#FFA000"/>
  <line x1="130" y1="180" x2="382" y2="180" stroke="#FFB300" stroke-width="8"/>
  <line x1="140" y1="260" x2="372" y2="260" stroke="#FFB300" stroke-width="8"/>
  <line x1="150" y1="340" x2="362" y2="340" stroke="#FFB300" stroke-width="8"/>
  <line x1="200" y1="120" x2="190" y2="410" stroke="#FFB300" stroke-width="8"/>
  <line x1="256" y1="100" x2="256" y2="415" stroke="#FF8F00" stroke-width="10"/>
  <line x1="312" y1="120" x2="322" y2="410" stroke="#FFB300" stroke-width="8"/>
</svg>""",

        # 55) 皮 (가죽 피)
        "皮": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#EFEBE9"/>
  <path d="M220 60 Q256 50 292 60 Q340 100 420 110 Q400 180 360 210 Q420 300 440 390 Q360 400 310 360 Q256 420 202 360 Q152 400 72 390 Q92 300 152 210 Q112 180 92 110 Q172 100 220 60 Z" fill="#D7CCC8" stroke="#5D4037" stroke-width="14"/>
  <ellipse cx="256" cy="220" rx="30" ry="18" fill="#8D6E63"/>
  <ellipse cx="190" cy="280" rx="24" ry="14" fill="#8D6E63"/>
  <ellipse cx="320" cy="280" rx="24" ry="14" fill="#8D6E63"/>
</svg>""",

        # 56) 瓜 (오이 과)
        "瓜": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#F1F8E9"/>
  <path d="M60 100 Q180 60 256 120 Q340 180 452 110" fill="none" stroke="#558B2F" stroke-width="14" stroke-linecap="round"/>
  <path d="M180 80 Q160 30 130 50 Q120 80 150 90" fill="none" stroke="#7CB342" stroke-width="8"/>
  <ellipse cx="256" cy="290" rx="120" ry="150" fill="#FDD835" stroke="#F57F17" stroke-width="14"/>
  <path d="M256 140 L256 120" stroke="#558B2F" stroke-width="14" stroke-linecap="round"/>
  <path d="M256 140 Q210 290 256 440" fill="none" stroke="#FFF9C4" stroke-width="10"/>
  <path d="M256 140 Q170 290 216 430" fill="none" stroke="#FFF9C4" stroke-width="10"/>
  <path d="M256 140 Q342 290 296 430" fill="none" stroke="#FFF9C4" stroke-width="10"/>
</svg>""",

        # 57) 燕 (제비 연)
        "燕": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E3F2FD"/>
  <path d="M256 80 Q290 120 290 200 L440 250 Q300 270 280 340 L340 450 L256 380 L172 450 L232 340 Q212 270 72 250 L222 200 Q222 120 256 80 Z" fill="#263238" stroke="#102027" stroke-width="8"/>
  <ellipse cx="256" cy="250" rx="36" ry="60" fill="#ECEFF1"/>
  <circle cx="256" cy="130" r="20" fill="#D32F2F"/>
  <polygon points="256,50 248,80 264,80" fill="#FFA000"/>
  <circle cx="248" cy="95" r="4" fill="#FFFFFF"/>
  <circle cx="264" cy="95" r="4" fill="#FFFFFF"/>
</svg>""",

        # 58) 鬯 (울창주 창)
        "鬯": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#FFF8E1"/>
  <path d="M120 180 L392 180 L350 420 L162 420 Z" fill="#D7CCC8" stroke="#4E342E" stroke-width="16"/>
  <path d="M220 200 Q200 130 160 140 Q180 190 220 200 Z" fill="#4CAF50"/>
  <path d="M292 200 Q312 130 352 140 Q332 190 292 200 Z" fill="#66BB6A"/>
  <circle cx="256" cy="300" r="40" fill="#FFC107" stroke="#FFA000" stroke-width="8"/>
  <circle cx="256" cy="300" r="20" fill="#FFE082"/>
  <line x1="256" y1="300" x2="380" y2="80" stroke="#00796B" stroke-width="14" stroke-linecap="round"/>
</svg>""",

        # 59) 鬲 (솥 력)
        "鬲": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#EFEBE9"/>
  <rect x="140" y="100" width="232" height="36" rx="8" fill="#8D6E63" stroke="#4E342E" stroke-width="12"/>
  <path d="M150 136 C100 220 80 320 120 440 L170 440 C190 350 210 320 256 320 C302 320 322 350 342 440 L392 440 C432 320 412 220 362 136 Z" fill="#A1887F" stroke="#4E342E" stroke-width="16"/>
  <line x1="160" y1="210" x2="352" y2="210" stroke="#4E342E" stroke-width="8" stroke-dasharray="12 12"/>
  <line x1="180" y1="260" x2="332" y2="260" stroke="#4E342E" stroke-width="8" stroke-dasharray="12 12"/>
</svg>""",

        # 60) 原 (언덕/근원 원)
        "原": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="64" fill="#E0F2F1"/>
  <path d="M60 80 L440 80 L440 140 L160 140 L160 440 L60 440 Z" fill="#78909C" stroke="#37474F" stroke-width="14"/>
  <circle cx="310" cy="270" r="70" fill="#00B0FF" stroke="#0091EA" stroke-width="12"/>
  <circle cx="310" cy="270" r="45" fill="#E1F5FE"/>
  <path d="M310 270 Q380 340 430 420" fill="none" stroke="#00B0FF" stroke-width="14" stroke-linecap="round"/>
  <path d="M280 310 Q310 380 340 440" fill="none" stroke="#40C4FF" stroke-width="12" stroke-linecap="round"/>
  <circle cx="340" cy="220" r="14" fill="#00B0FF"/>
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
    "川": "CUSTOM",    # 🌊 [CUSTOM] 3줄기 흐르는 강물
    "雨": "1f327",     # 🌧️ 비구름과 빗방울
    "土": "CUSTOM",    # 🪴 [CUSTOM] 비옥한 흙더미와 지층
    "石": "1faa8",     # 🪨 단단한 바위/돌
    "風": "1f4a8",     # 💨 바람/돌풍
    "雲": "2601",      # ☁️ 뭉게구름
    "泉": "CUSTOM",    # ⛲ [CUSTOM] 바위틈에서 솟구치는 옹달샘
    "谷": "1f3de",     # 🏞️ 깊은 산골짜기
    "原": "CUSTOM",    # 🏛️ [CUSTOM] 언덕 아래 샘솟는 원천
    "氣": "CUSTOM",    # 🌀 [CUSTOM] 피어오르는 김과 생명 기운

    # 2. 인체 & 사람 (28자)
    "大": "CUSTOM",    # 🧍 [CUSTOM] 팔다리를 크게 벌린 사람
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
    "毛": "CUSTOM",    # 🦱 [CUSTOM] 부드러운 털 가닥
    "皮": "CUSTOM",    # 🐆 [CUSTOM] 벗겨서 펼쳐놓은 동물 가죽
    "爪": "CUSTOM",    # 🦅 [CUSTOM] 맹수의 날카로운 갈퀴 발톱
    "角": "1f98c",     # 🦌 솟아난 사슴 뿔
    "母": "1f931",     # 🤱 아기를 품에 안은 어머니
    "父": "1f468",     # 👨 수염 난 다정한 아버지
    "老": "1f474",     # 👴 지팡이를 짚은 노인
    "臣": "CUSTOM",    # 💂 [CUSTOM] 홀을 들고 공손히 고개 숙인 신하

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
    "尾": "CUSTOM",    # 🦊 [CUSTOM] 말려 올라간 탐스러운 꼬리
    "兔": "1f407",     # 🐇 긴 귀 토끼
    "鼠": "1f401",     # 🐁 쪼르르 쥐
    "豚": "1f437",     # 🐷 통통한 아기돼지
    "豸": "1f406",     # 🐆 몸을 웅크린 맹수 표범
    "燕": "CUSTOM",    # 🐦 [CUSTOM] 갈라진 제비꼬리 제비
    "貝": "1f41a",     # 🐚 바다 조개껍데기
    "蛙": "1f438",     # 🐸 개구리
    "鶴": "CUSTOM",    # 🦩 [CUSTOM] 붉은 정수리의 우아한 단정학
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
    "竹": "CUSTOM",    # 🎋 [CUSTOM] 마디와 잎이 있는 대나무
    "禾": "1f33e",     # 🌾 고개 숙인 벼 이삭
    "米": "CUSTOM",    # 🍚 [CUSTOM] 흩어진 쌀알들
    "果": "1f34e",     # 🍎 나무에 열린 과일 사과
    "瓜": "CUSTOM",    # 🍈 [CUSTOM] 덩굴에 달린 참외/오이
    "桑": "1f343",     # 🍃 뽕나무 잎
    "麥": "CUSTOM",    # 🌾 [CUSTOM] 긴 수염의 보리 이삭
    "麻": "1f9f5",     # 🧵 삼베 실타래
    "豆": "CUSTOM",    # 🫘 [CUSTOM] 꼬투리 속 3알의 콩
    "黍": "1f33e",     # 🌾 기장 곡식
    "林": "CUSTOM",    # 🌲🌲 [CUSTOM] 2그루 수풀
    "森": "CUSTOM",    # 🌲🌲🌲 [CUSTOM] 3그루 울창한 삼림
    "根": "CUSTOM",    # 🥕 [CUSTOM] 땅속 깊은 나무 뿌리
    "枝": "CUSTOM",    # 🪵 [CUSTOM] 뻗어나간 나뭇가지와 잎
    "葉": "1f343",     # 🍃 푸른 나뭇잎
    "芽": "1f331",     # 🌱 땅을 뚫고 나온 새싹
    "苗": "CUSTOM",    # 🌱 [CUSTOM] 논에 심은 어린 볏모
    "田": "CUSTOM",    # 🟩 [CUSTOM] 바둑판식 논밭이랑
    "井": "CUSTOM",    # 🧱 [CUSTOM] 정자(井)형 돌틀 우물
    "圃": "CUSTOM",    # 🥬 [CUSTOM] 울타리 두른 채소 텃밭

    # 5. 도구 & 무기 (34자)
    "車": "CUSTOM",    # 🛞 [CUSTOM] 바퀴살 달린 옛 목조 수레
    "舟": "CUSTOM",    # ⛵ [CUSTOM] 노가 딸린 통나무 나룻배
    "刀": "1f5e1",     # 🗡️ 칼/단도
    "弓": "1f3f9",     # 🏹 활과 화살
    "矢": "CUSTOM",    # 🎯 [CUSTOM] 깃 달린 날아가는 화살
    "戈": "CUSTOM",    # 🔱 [CUSTOM] 고대 ㄱ자 꺾창
    "矛": "CUSTOM",    # 🗡️ [CUSTOM] 찌르는 장창
    "斤": "1fa93",     # 🪓 도끼
    "斧": "1fa93",     # 🪓 큰 손도끼
    "網": "CUSTOM",    # 🕸️ [CUSTOM] 물고기 잡는 투망 어망
    "鼎": "CUSTOM",    # 🍲 [CUSTOM] 세 발 달린 청동 솥
    "鬲": "CUSTOM",    # 🫕 [CUSTOM] 세 발 달린 토기 솥
    "皿": "CUSTOM",    # 🍽️ [CUSTOM] 오목한 도자기 그릇
    "壺": "1f3fa",     # 🏺 도자기 항아리 병
    "缶": "CUSTOM",    # 🥫 [CUSTOM] 흙으로 빚은 옹기/장군
    "臼": "CUSTOM",    # 🥣 [CUSTOM] 곡식 찧는 절구
    "杵": "CUSTOM",    # 🥢 [CUSTOM] 절구 방망이 공이
    "箕": "CUSTOM",    # 🧺 [CUSTOM] 곡식 까부르는 키
    "帚": "1f9f9",     # 🧹 먼지 쓰는 빗자루
    "卓": "CUSTOM",    # 🪑 [CUSTOM] 원목 사각 식탁 탁자
    "几": "CUSTOM",    # 🪑 [CUSTOM] 기대는 전통 안석
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
    "堂": "CUSTOM",    # 🏛️ [CUSTOM] 축대 위의 큰 대당
    "屋": "1f3e0",     # 🏠 기와집
    "衣": "1f458",     # 👘 옷
    "巾": "CUSTOM",    # 🧣 [CUSTOM] 걸이에 걸린 수건 천
    "帶": "CUSTOM",    # 🥋 [CUSTOM] 옥 장식 비단 허리띠
    "履": "CUSTOM",    # 👞 [CUSTOM] 코가 들린 비단 꽃신
    "冠": "CUSTOM",    # 👑 [CUSTOM] 면류관과 전통 관모
    "傘": "2602",      # ☂️ 우산
    "食": "1f371",     # 🍱 음식/밥
    "酒": "1f376",     # 🍶 술병과 잔
    "酉": "1f3fa",     # 🏺 빚은 술 항아리
    "鬯": "CUSTOM",    # 🍷 [CUSTOM] 제사용 울창주 항아리와 국자
    "冊": "CUSTOM",    # 📖 [CUSTOM] 끈으로 엮은 대나무 죽간
    "聿": "CUSTOM",    # 🖌️ [CUSTOM] 손에 쥔 서예 붓
    "筆": "1f58c",     # 🖌️ 서예 붓
    "墨": "CUSTOM",    # ✒️ [CUSTOM] 황금 각인 명품 먹과 먹물
    "紙": "1f4c4",     # 📄 종이
    "硯": "CUSTOM",    # 🪨 [CUSTOM] 먹물 고인 석조 벼루
    "錢": "1fa99",     # 🪙 엽전 동전
    "玉": "CUSTOM",    # 💎 [CUSTOM] 3알을 꿴 비취 옥패
    "瓦": "CUSTOM",    # 🧱 [CUSTOM] 한옥 지붕 기와
    "郭": "CUSTOM",    # 🏯 [CUSTOM] 아치문이 있는 성곽 성벽
    "壘": "CUSTOM",    # 🏰 [CUSTOM] 3단 군사 방어 보루
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
