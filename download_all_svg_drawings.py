"""
160개 상형한자 직관적 오픈 벡터 일러스트(Twemoji / OpenMoji) 자동 매핑 및 다운로더
- 어린이와 성인 모두 한눈에 직관적으로 이해할 수 있는 최고 품질의 컬러 벡터 그래픽 매핑
- 파란색 단색 박스 문제를 해결하고, 원본 풀컬러 벡터 일러스트 보존
"""
import os
import sys
import urllib.request
import json

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

DRAWING_MAP = {
    # 1. 자연 & 천문
    "日": "2600",      # ☀️ 태양
    "月": "1f319",     # 🌙 초승달
    "山": "26f0",      # ⛰️ 산 봉우리
    "水": "1f4a7",     # 💧 맑은 물방울
    "火": "1f525",     # 🔥 활활 타는 불꽃
    "川": "1f3de",     # 🏞️ 굽이치는 하천/계곡
    "雨": "1f327",     # 🌧️ 비구름과 빗방울
    "土": "1f331",     # 🌱 땅 위의 흙과 새싹
    "石": "1faa8",     # 🪨 단단한 바위/돌
    "風": "1f4a8",     # 💨 쌩쌩 부는 바람
    "雲": "2601",      # ☁️ 뭉게구름
    "泉": "26f2",      # ⛲ 솟아나는 샘물
    "谷": "1f3de",     # 🏞️ 깊은 산골짜기
    "原": "1f33e",     # 🌾 넓은 들판
    "氣": "1f4a8",     # 💨 공기/기운

    # 2. 인체 & 사람
    "大": "1f9cd",     # 🧍 팔다리를 편 큰 사람
    "人": "1f464",     # 👤 사람의 실루엣
    "女": "1f469",     # 👩 여인
    "子": "1f476",     # 👶 어린 아기
    "目": "1f441",     # 👁️ 사람의 눈
    "耳": "1f442",     # 👂 소리를 듣는 귀
    "口": "1f444",     # 👄 말하는 입
    "手": "270b",      # ✋ 다섯 손가락 손
    "足": "1f9b6",     # 🦶 걷는 발
    "心": "2764",      # ❤️ 따뜻한 심장/마음
    "首": "1f451",     # 👑 머리/우두머리
    "頭": "1f9e0",     # 🧠 생각하는 머리/뇌
    "面": "1f600",     # 😀 사람의 얼굴
    "齒": "1f9b7",     # 🦷 하얗고 고른 치아
    "舌": "1f445",     # 👅 입 밖의 붉은 혀
    "鼻": "1f443",     # 👃 숨 쉬는 코
    "身": "1f9cd",     # 🧍 사람의 신체
    "骨": "1f9b4",     # 🦴 뼈대
    "肉": "1f969",     # 🥩 붉은 살코기
    "血": "1fa78",     # 🩸 붉은 핏방울
    "毛": "1f9b1",     # 🦱 부드러운 털/머리칼
    "皮": "1f9e5",     # 🧥 짐승의 털가죽
    "爪": "1f485",     # 💅 날카로운 손톱
    "角": "1f98c",     # 🦌 뾰족한 사슴 뿔
    "母": "1f931",     # 🤱 아기를 안은 어머니
    "父": "1f468",     # 👨 다정한 아버지
    "老": "1f474",     # 👴 지팡이를 짚은 할아버지
    "臣": "1f482",     # 💂 충성스러운 신하

    # 3. 동물 & 곤충
    "牛": "1f402",     # 🐂 뿔 달린 황소
    "馬": "1f40e",     # 🐎 달리는 말
    "羊": "1f411",     # 🐑 포근한 양
    "豕": "1f416",     # 🐖 통통한 돼지
    "犬": "1f415",     # 🐕 꼬리 흔드는 개
    "鳥": "1f426",     # 🐦 지저귀는 새
    "隹": "1f424",     # 🐤 귀여운 작은 새
    "魚": "1f41f",     # 🐟 헤엄치는 물고기
    "蟲": "1f41b",     # 🐛 꿈틀거리는 벌레
    "龜": "1f422",     # 🐢 엉금엉금 거북이
    "象": "1f418",     # 🐘 긴 코 코끼리
    "鹿": "1f98c",     # 🦌 멋진 뿔 사슴
    "虎": "1f405",     # 🐅 용맹한 호랑이
    "蛇": "1f40d",     # 🐍 스르륵 기는 뱀
    "龍": "1f409",     # 🐉 신비로운 용
    "羽": "1fab6",     # 🪶 가벼운 깃털
    "尾": "1f98a",     # 🦊 탐스러운 꼬리
    "兔": "1f407",     # 🐇 깡충깡충 토끼
    "鼠": "1f401",     # 🐁 쪼르르 쥐
    "豚": "1f437",     # 🐷 귀여운 돼지
    "豸": "1f406",     # 🐆 먹이를 노리는 표범
    "燕": "1f426",     # 🐦 제비
    "貝": "1f41a",     # 🐚 예쁜 조개껍데기
    "蛙": "1f438",     # 🐸 개굴개굴 개구리
    "鶴": "1f9a9",     # 🦩 다리가 긴 두루미/학
    "鵝": "1f9a2",     # 🦢 우아한 백조/거위
    "鷹": "1f985",     # 🦅 하늘의 제왕 매/독수리
    "蜂": "1f41d",     # 🐝 붕붕 날아다니는 꿀벌
    "蝶": "1f98b",     # 🦋 아름다운 나비
    "蛛": "1f577",     # 🕷️ 거미
    "蟻": "1f41c",     # 🐜 부지런한 개미
    "熊": "1f43b",     # 🐻 늠름한 곰

    # 4. 식물 & 농경
    "木": "1f333",     # 🌳 울창한 나무
    "艸": "1f33f",     # 🌿 파릇파릇한 풀
    "竹": "1f38b",     # 🎋 곧은 대나무
    "禾": "1f33e",     # 🌾 누렇게 익은 벼
    "米": "1f35a",     # 🍚 하얀 쌀밥
    "果": "1f34e",     # 🍎 빨간 사과 열매
    "瓜": "1f952",     # 🥒 길쭉한 오이
    "桑": "1f343",     # 🍃 싱그러운 뽕나무 잎
    "麥": "1f33e",     # 🌾 구수한 보리 이삭
    "麻": "1f9f5",     # 🧵 삼베 실/삼
    "豆": "1fac8",     # 🫘 밭에서 나는 콩
    "黍": "1f33e",     # 🌾 기장 곡식
    "林": "1f332",     # 🌲 나무가 모인 숲
    "森": "1f332",     # 🌲 울창하고 깊은 숲
    "根": "1f955",     # 🥕 땅속 깊은 뿌리
    "枝": "1fab5",     # 🪵 뻗어나간 나뭇가지
    "葉": "1f343",     # 🍃 바람에 날리는 나뭇잎
    "花": "1f338",     # 🌸 화사한 꽃
    "芽": "1f331",     # 🌱 갓 돋아난 새싹
    "苗": "1f331",     # 🌱 푸른 모
    "田": "1f3de",     # 🏞️ 넓은 논밭
    "井": "1f9f1",     # 🧱 우물틀
    "圃": "1f96c",     # 🥬 신선한 채소밭
    "穀": "1f33e",     # 🌾 영양 가득한 곡식

    # 5. 도구 & 무기
    "車": "1f697",     # 🚗 바퀴 달린 자동차/수레
    "舟": "26f5",      # ⛵ 물 위의 돛단배
    "刀": "1f5e1",     # 🗡️ 날카로운 칼
    "弓": "1f3f9",     # 🏹 당겨진 활
    "矢": "1f3af",     # 🎯 날아가는 화살과 과녁
    "戈": "1f531",     # 🔱 옛 전쟁용 꺾창
    "矛": "1f5e1",     # 🗡️ 찌르는 긴 창
    "斤": "1fa93",     # 🪓 나무 찍는 도끼
    "斧": "1fa93",     # 🪓 큰 손도끼
    "網": "1f578",     # 🕸️ 촘촘한 그물
    "鼎": "1f372",     # 🍲 세 다리 솥
    "鬲": "1fad5",     # 🫕 끓이는 솥
    "皿": "1f37d",     # 🍽️ 음식을 담는 접시
    "壺": "1f3fa",     # 🏺 도자기 항아리 병
    "缶": "1f96b",     # 🥫 둥근 캔/장군
    "臼": "1f963",     # 🥣 곡식 찧는 절구
    "杵": "1f962",     # 🥢 절구 방망이
    "箕": "1f9fa",     # 🧺 대나무 키/바구니
    "帚": "1f9f9",     # 🧹 먼지 쓰는 빗자루
    "卓": "1fa91",     # 🪑 다리 달린 탁자
    "几": "1fa91",     # 🪑 작은 안석 탁자
    "床": "1f6cf",     # 🛏️ 편안한 침상/마루
    "繩": "1fa92",     # 🪢 튼튼한 밧줄
    "索": "1fa92",     # 🪢 꼬아 만든 노끈
    "針": "1faa1",     # 🪡 뾰족한 바늘과 실
    "鏡": "1fa9e",     # 🪞 비추는 거울
    "鐘": "1f514",     # 🔔 맑게 울리는 종
    "鼓": "1f941",     # 🥁 둥둥 치는 북
    "磬": "1f3b5",     # 🎵 맑은 음을 내는 경쇠
    "笛": "1fa88",     # 🪈 멜로디 피리
    "琴": "1f3b9",     # 🎹 아름다운 줄 악기 거문고
    "管": "1f9ea",     # 🧪 속이 빈 대롱/시험관
    "印": "1f4dc",     # 📜 붉은 도장이 찍힌 문서
    "楯": "1f6e1",     # 🛡️ 막아내는 방패

    # 6. 의식주 & 건축 & 문화
    "門": "1f6aa",     # 🚪 활짝 열리는 문
    "戶": "1f6aa",     # 🚪 외짝 방문
    "宮": "1f3f0",     # 🏰 웅장한 궁궐
    "室": "1f3eb",     # 🏫 방/교실
    "堂": "1f3db",     # 🏛️ 위엄 있는 큰 대당
    "屋": "1f3e0",     # 🏠 아늑한 집
    "衣": "1f458",     # 👘 아름다운 옷
    "巾": "1f9e3",     # 🧣 부드러운 수건/목도리
    "帶": "1f94b",     # 🥋 허리에 매는 띠
    "履": "1f45e",     # 👞 신고 걷는 신발
    "冠": "1f451",     # 👑 머리에 쓰는 왕관/갓
    "傘": "2602",      # ☂️ 비를 막는 우산
    "食": "1f371",     # 🍱 맛있는 밥/음식
    "酒": "1f376",     # 🍶 향긋한 전통 술
    "酉": "1f376",     # 🍶 빚은 술병
    "鬯": "1f377",     # 🍷 제사용 향기로운 술
    "冊": "1f4d6",     # 📖 펼쳐진 책
    "聿": "1f58c",     # 🖌️ 글씨를 쓰는 붓
    "筆": "1f58c",     # 🖌️ 먹을 묻힌 서예 붓
    "墨": "2712",      # ✒️ 검고 진한 먹물
    "紙": "1f4c4",     # 📄 새하얀 종이
    "硯": "1faa8",     # 🪨 먹을 가는 돌벼루
    "錢": "1fa99",     # 🪙 반짝이는 동전/돈
    "玉": "1f48e",     # 💎 영롱한 옥/보석
    "瓦": "1f9f1",     # 🧱 단단히 구운 기와
    "郭": "1f3ef",     # 🏯 도성을 둘러싼 성곽
    "壘": "1f3f0",     # 🏰 군사 요새 보루
}

def download_all():
    os.makedirs("assets/svg_drawings", exist_ok=True)
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
    from hanzi_data import HANZI_DATABASE

    success_count = 0
    updated_db = {}

    for char, data in HANZI_DATABASE.items():
        clean_char = char.replace("/", "_")
        emoji_code = DRAWING_MAP.get(char, DRAWING_MAP.get(clean_char, "2728"))
        out_svg = os.path.join("assets", "svg_drawings", f"{clean_char}_drawing.svg")
        os.makedirs(os.path.dirname(out_svg), exist_ok=True)
        
        # 1. Twemoji 다운로드 시도
        url_twemoji = f"https://raw.githubusercontent.com/twitter/twemoji/master/assets/svg/{emoji_code}.svg"
        url_openmoji = f"https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/svg/{emoji_code.upper()}.svg"
        
        svg_content = None
        for url in [url_twemoji, url_openmoji]:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=4) as resp:
                    svg_content = resp.read().decode("utf-8")
                    break
            except Exception:
                continue

        if not svg_content:
            # 폴백: 깔끔한 컬러 심볼 SVG
            svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <circle cx="512" cy="512" r="460" fill="#FEF3C7" stroke="#F59E0B" stroke-width="32"/>
  <text x="512" y="600" font-size="380" font-family="Arial, sans-serif" font-weight="bold" fill="#D97706" text-anchor="middle">{char}</text>
</svg>"""

        with open(out_svg, "w", encoding="utf-8") as f:
            f.write(svg_content)

        data["drawing_svg"] = svg_content
        updated_db[char] = data
        success_count += 1

    print(f"🎉 총 {success_count}개 상형한자 직관적 컬러 벡터 일러스트 다운로드 및 매핑 완료!")

    # hanzi_data.py 갱신
    lines = [
        '"""',
        '상형문자 및 한국식 한자(번체/정자체) 160자 마스터 메타데이터 & 직관적 컬러 벡터 SVG 데이터베이스',
        f'- 총 고유 등록 상형한자: {len(updated_db)}자 (중복 없음)',
        '- 컬러 벡터 일러스트(Twemoji/OpenMoji) 매핑 완료',
        '"""',
        '',
        'HANZI_DATABASE = {'
    ]

    for char, d in updated_db.items():
        lines.append(f'    "{char}": {{')
        lines.append(f'        "char": "{d["char"]}",')
        lines.append(f'        "stroke_count": {d["stroke_count"]},')
        lines.append(f'        "hun_eum": "{d["hun_eum"]}",')
        lines.append(f'        "hun_eum_en": "{d["hun_eum_en"]}",')
        lines.append(f'        "sound_desc": "{d["sound_desc"]}",')
        lines.append(f'        "example_word": "{d["example_word"]}",')
        lines.append(f'        "example_word_desc": "{d["example_word_desc"]}",')
        lines.append(f'        "stroke_names": {json.dumps(d.get("stroke_names", []), ensure_ascii=False)},')
        lines.append(f'        "drawing_svg": """{d["drawing_svg"].strip()}"""')
        lines.append('    },')

    lines.append('}')
    lines.append('')

    with open("src/hanzi_data.py", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("✅ src/hanzi_data.py 업데이트 완료!")

if __name__ == "__main__":
    download_all()
