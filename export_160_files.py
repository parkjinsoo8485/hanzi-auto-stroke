import os
import sys
import json
import re

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(base_dir, "src"))

from hanzi_data import HANZI_DATABASE
from build_160_database import RAW_CHARS

CATEGORIES = [
    ("자연 & 천문 (15자)", 0, 15),
    ("인체 & 사람 (28자)", 15, 43),
    ("동물 & 곤충 (32자)", 43, 75),
    ("식물 & 농경 (24자)", 75, 99),
    ("도구 & 무기 & 기물 (34자)", 99, 133),
    ("의식주 & 건축 & 문화 (27자)", 133, 160)
]

print(f"Total RAW_CHARS: {len(RAW_CHARS)}, Total DB keys: {len(HANZI_DATABASE)}")

# 1. JSON 파일 저장
json_data = []
for i, item in enumerate(RAW_CHARS, 1):
    char, hun_eum, hun_eum_en, sound_desc, example_word, example_word_desc, stroke_count = item
    clean_char = char.replace("/", "_")
    
    # 카테고리 판별
    cat_name = "기타"
    for c_title, start_idx, end_idx in CATEGORIES:
        if start_idx <= (i - 1) < end_idx:
            cat_name = c_title.split(" (")[0]
            break
            
    # SVG 드로잉
    db_item = HANZI_DATABASE.get(char, {})
    drawing_svg = db_item.get("drawing_svg", "")
    
    json_data.append({
        "id": i,
        "category": cat_name,
        "char": char,
        "stroke_count": stroke_count,
        "hun_eum": hun_eum,
        "hun_eum_en": hun_eum_en,
        "origin_desc": sound_desc,
        "example_word": example_word,
        "example_word_desc": example_word_desc,
        "svg_file": f"assets/svg_drawings/{clean_char}_drawing.svg",
        "drawing_svg": drawing_svg
    })

json_path = os.path.join(base_dir, "HANZI_160_LIST.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)
print(f"✅ JSON 저장 완료: {json_path}")

# 2. Markdown 문서 저장
md_path = os.path.join(base_dir, "HANZI_160_LIST.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("# 📚 160개 대표 상형한자(象形漢字) 마스터 리스트 & 직관적 이미지 안내\n\n")
    f.write("> 본 문서는 고대 사물의 모양을 본떠 만든 **160개의 핵심 상형한자**를 6가지 대주제별로 분류하고, 각 한자의 훈음, 영문 의미, 상형 유래, 실생활 활용 단어, 획수 및 직관적 일러스트(SVG) 파일 링크를 체계적으로 정리한 마스터 데이터 문서입니다.\n\n")
    f.write("---\n\n")
    f.write("## 📌 목차\n")
    for cat_name, s, e in CATEGORIES:
        f.write(f"- [{cat_name}](#{cat_name.replace(' ', '-').replace('&', '').replace('(', '').replace(')', '')})\n")
    f.write("\n---\n\n")
    
    for cat_title, s, e in CATEGORIES:
        f.write(f"## {cat_title}\n\n")
        f.write("| 번호 | 한자 | 훈음 | 영문 의미 | 상형 기원 및 유래 | 실생활 단어 | 획수 | 직관적 이미지 |\n")
        f.write("| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :---: |\n")
        
        for idx in range(s, e):
            item = RAW_CHARS[idx]
            char, hun_eum, hun_eum_en, sound_desc, example_word, example_word_desc, stroke_count = item
            clean_char = char.replace("/", "_")
            svg_link = f"[보기](assets/svg_drawings/{clean_char}_drawing.svg)"
            f.write(f"| {idx+1} | **{char}** | {hun_eum} | {hun_eum_en} | {sound_desc} | `{example_word}` ({example_word_desc}) | {stroke_count}획 | {svg_link} |\n")
        f.write("\n")

print(f"✅ Markdown 저장 완료: {md_path}")

# 3. 브라우저에서 바로 볼 수 있는 인터랙티브 HTML 갤러리 뷰어 생성
html_path = os.path.join(base_dir, "HANZI_160_GALLERY.html")

cards_html = []
for item in json_data:
    svg_tag = item["drawing_svg"]
    # Ensure svg is well formatted
    if not svg_tag or "<svg" not in svg_tag:
        clean_char = item["char"].replace("/", "_")
        svg_tag = f'<img src="assets/svg_drawings/{clean_char}_drawing.svg" alt="{item["char"]}" />'
        
    card = f"""
    <div class="hanzi-card" data-category="{item['category']}" data-char="{item['char']}" data-huneum="{item['hun_eum']}" data-en="{item['hun_eum_en']}">
        <div class="card-header">
            <span class="card-id">#{item['id']}</span>
            <span class="card-cat">{item['category']}</span>
            <span class="card-strokes">{item['stroke_count']}획</span>
        </div>
        <div class="visual-box">
            <div class="hanzi-char">{item['char']}</div>
            <div class="arrow">➔</div>
            <div class="drawing-box">{svg_tag}</div>
        </div>
        <div class="card-body">
            <div class="hun-eum">{item['hun_eum']}</div>
            <div class="hun-eum-en">{item['hun_eum_en']}</div>
            <div class="origin-desc"><span class="badge">상형 유래</span> {item['origin_desc']}</div>
            <div class="example-word"><span class="badge">대표 단어</span> <strong>{item['example_word']}</strong> - {item['example_word_desc']}</div>
        </div>
    </div>
    """
    cards_html.append(card)

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>160개 상형한자 직관적 비주얼 갤러리</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;800&family=Noto+Serif+KR:wght@600;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #0F172A;
            --surface: #1E293B;
            --surface-card: #243248;
            --text-main: #F8FAFC;
            --text-muted: #94A3B8;
            --accent: #F59E0B;
            --accent-glow: rgba(245, 158, 11, 0.25);
            --primary: #38BDF8;
            --border: #334155;
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        body {{
            font-family: 'Noto Sans KR', -apple-system, sans-serif;
            background-color: var(--bg);
            color: var(--text-main);
            min-height: 100vh;
            padding: 2rem 1.5rem;
        }}
        .header {{
            max-width: 1400px;
            margin: 0 auto 2.5rem;
            text-align: center;
        }}
        .header h1 {{
            font-family: 'Noto Serif KR', serif;
            font-size: 2.75rem;
            font-weight: 900;
            background: linear-gradient(135deg, #FDE68A 0%, #F59E0B 50%, #F97316 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.75rem;
            letter-spacing: -0.02em;
        }}
        .header p {{
            font-size: 1.15rem;
            color: var(--text-muted);
            max-width: 700px;
            margin: 0 auto 1.75rem;
            line-height: 1.6;
        }}
        
        .controls-container {{
            max-width: 1400px;
            margin: 0 auto 2rem;
            display: flex;
            flex-direction: column;
            gap: 1rem;
            background: var(--surface);
            padding: 1.25rem 1.5rem;
            border-radius: 1rem;
            border: 1px solid var(--border);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        }}
        .search-bar {{
            display: flex;
            gap: 1rem;
        }}
        .search-input {{
            flex: 1;
            padding: 0.85rem 1.25rem;
            border-radius: 0.6rem;
            border: 1px solid var(--border);
            background: var(--bg);
            color: #fff;
            font-size: 1.05rem;
            outline: none;
            transition: all 0.2s ease;
        }}
        .search-input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
        }}
        .filter-tabs {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}
        .filter-btn {{
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            border: 1px solid var(--border);
            background: var(--surface-card);
            color: var(--text-muted);
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .filter-btn:hover {{
            background: var(--border);
            color: #fff;
        }}
        .filter-btn.active {{
            background: var(--accent);
            color: #0F172A;
            border-color: var(--accent);
            box-shadow: 0 0 12px var(--accent-glow);
        }}

        .stats-bar {{
            max-width: 1400px;
            margin: 0 auto 1.5rem;
            font-size: 0.95rem;
            color: var(--text-muted);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .gallery-grid {{
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
            gap: 1.5rem;
        }}

        .hanzi-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 1.25rem;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}
        .hanzi-card:hover {{
            transform: translateY(-5px);
            border-color: var(--accent);
            box-shadow: 0 12px 28px -6px rgba(0, 0, 0, 0.4), 0 0 15px var(--accent-glow);
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem 1.25rem;
            background: rgba(0, 0, 0, 0.2);
            border-bottom: 1px solid var(--border);
            font-size: 0.8rem;
            font-weight: 600;
        }}
        .card-id {{
            color: var(--accent);
            font-weight: 800;
        }}
        .card-cat {{
            color: var(--primary);
        }}
        .card-strokes {{
            color: var(--text-muted);
            background: var(--surface-card);
            padding: 0.2rem 0.5rem;
            border-radius: 0.3rem;
        }}

        .visual-box {{
            display: flex;
            align-items: center;
            justify-content: space-around;
            padding: 1.25rem;
            background: linear-gradient(180deg, rgba(36, 50, 72, 0.4) 0%, rgba(15, 23, 42, 0.6) 100%);
            border-bottom: 1px solid var(--border);
            min-height: 140px;
        }}
        .hanzi-char {{
            font-family: 'Noto Serif KR', serif;
            font-size: 4rem;
            font-weight: 900;
            color: #F8FAFC;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
            line-height: 1;
        }}
        .arrow {{
            font-size: 1.5rem;
            color: var(--accent);
            opacity: 0.8;
        }}
        .drawing-box {{
            width: 90px;
            height: 90px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #FFFFFF;
            border-radius: 1rem;
            padding: 0.4rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        }}
        .drawing-box svg, .drawing-box img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}

        .card-body {{
            padding: 1.25rem;
            display: flex;
            flex-direction: column;
            gap: 0.6rem;
            flex: 1;
        }}
        .hun-eum {{
            font-size: 1.4rem;
            font-weight: 800;
            color: #FEF08A;
        }}
        .hun-eum-en {{
            font-size: 0.95rem;
            color: var(--primary);
            font-weight: 600;
            margin-bottom: 0.25rem;
        }}
        .origin-desc, .example-word {{
            font-size: 0.9rem;
            color: #CBD5E1;
            line-height: 1.45;
        }}
        .badge {{
            display: inline-block;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.15rem 0.45rem;
            border-radius: 0.3rem;
            margin-right: 0.3rem;
            background: #334155;
            color: #94A3B8;
        }}
        .example-word .badge {{
            background: #0284C7;
            color: #E0F2FE;
        }}
        .origin-desc .badge {{
            background: #D97706;
            color: #FEF3C7;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>✨ 160개 상형한자(象形漢字) 비주얼 아카이브</h1>
        <p>고대 사물의 형태에서 글자가 탄생한 원리를 한눈에 비교하고 학습할 수 있는 인터랙티브 상형한자 사전입니다.</p>
    </div>

    <div class="controls-container">
        <div class="search-bar">
            <input type="text" id="searchInput" class="search-input" placeholder="한자, 훈음(예: 날 일), 영문(Sun), 유래 검색...">
        </div>
        <div class="filter-tabs" id="filterTabs">
            <button class="filter-btn active" data-filter="all">전체 (160자)</button>
            <button class="filter-btn" data-filter="자연 & 천문">자연 & 천문 (15)</button>
            <button class="filter-btn" data-filter="인체 & 사람">인체 & 사람 (28)</button>
            <button class="filter-btn" data-filter="동물 & 곤충">동물 & 곤충 (32)</button>
            <button class="filter-btn" data-filter="식물 & 농경">식물 & 농경 (24)</button>
            <button class="filter-btn" data-filter="도구 & 무기 & 기물">도구 & 무기 & 기물 (34)</button>
            <button class="filter-btn" data-filter="의식주 & 건축 & 문화">의식주 & 건축 & 문화 (27)</button>
        </div>
    </div>

    <div class="stats-bar">
        <span id="resultCount">총 160개의 한자 표시 중</span>
        <span>정렬: 고대 유래 카테고리순</span>
    </div>

    <div class="gallery-grid" id="galleryGrid">
        {"".join(cards_html)}
    </div>

    <script>
        const searchInput = document.getElementById('searchInput');
        const filterBtns = document.querySelectorAll('.filter-btn');
        const cards = document.querySelectorAll('.hanzi-card');
        const resultCount = document.getElementById('resultCount');

        let currentFilter = 'all';

        function updateFilter() {{
            const query = searchInput.value.trim().toLowerCase();
            let count = 0;

            cards.forEach(card => {{
                const cat = card.getAttribute('data-category');
                const char = card.getAttribute('data-char');
                const huneum = card.getAttribute('data-huneum');
                const en = card.getAttribute('data-en').toLowerCase();
                const cardText = card.textContent.toLowerCase();

                const matchesCat = (currentFilter === 'all' || cat === currentFilter);
                const matchesQuery = !query || cardText.includes(query) || char.includes(query) || huneum.includes(query) || en.includes(query);

                if (matchesCat && matchesQuery) {{
                    card.style.display = 'flex';
                    count++;
                }} else {{
                    card.style.display = 'none';
                }}
            }});

            resultCount.textContent = `총 ${{count}}개의 한자 표시 중`;
        }}

        searchInput.addEventListener('input', updateFilter);

        filterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentFilter = btn.getAttribute('data-filter');
                updateFilter();
            }});
        }});
    </script>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ HTML 갤러리 저장 완료: {html_path}")
print("🎉 모든 160개 상형한자 데이터 및 직관적 이미지 매핑 파일 생성 완료!")
