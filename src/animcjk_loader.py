"""
AnimCJK 한국 한자(정자체/번체) 획순 SVG 자동 다운로드 및 붓 진행 경로(Medial) 추출 엔진
"""
import os
import re
import urllib.request

ANIMCJK_CACHE_DIR = "assets/animcjk_cache"
SVG_HANZI_DIR = "assets/svg_hanzi"

def fetch_animcjk_svg(char: str) -> str:
    """AnimCJK 한국 한자(svgsKo) 또는 번체(svgsZhHant) SVG 다운로드 및 캐시"""
    os.makedirs(ANIMCJK_CACHE_DIR, exist_ok=True)
    codepoint = ord(char)
    cache_path = os.path.join(ANIMCJK_CACHE_DIR, f"{codepoint}_{char}.svg")

    if os.path.exists(cache_path):
        with open(cache_path, "r", encoding="utf-8") as f:
            return f.read()

    urls = [
        f"https://raw.githubusercontent.com/parsimonhi/animCJK/master/svgsKo/{codepoint}.svg",
        f"https://raw.githubusercontent.com/parsimonhi/animCJK/master/svgsZhHant/{codepoint}.svg",
        f"https://raw.githubusercontent.com/parsimonhi/animCJK/master/svgsJa/{codepoint}.svg"
    ]

    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=5) as response:
                content = response.read().decode("utf-8")
                with open(cache_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"[AnimCJK] Downloaded {char} ({codepoint}) from {url}")
                return content
        except Exception as e:
            continue

    raise ValueError(f"AnimCJK에서 '{char}' (유니코드 {codepoint}) 데이터를 찾을 수 없습니다.")

def parse_animcjk_strokes(char: str):
    """
    AnimCJK SVG에서:
    1. 각 획의 해서체 윤곽선 (Outline)
    2. 각 획의 붓 진행 중심선 (Medial Path)
    3. 1024x1024 전역 좌표계 보존
    """
    svg_content = fetch_animcjk_svg(char)
    codepoint = ord(char)
    
    # 1. 외곽선 path 추출 (d1, d2, ...)
    outline_matches = re.findall(rf'<path\s+id="z{codepoint}d(\d+)"\s+d="([^"]+)"', svg_content)
    if not outline_matches:
        outline_matches = re.findall(r'<path\s+id="[^"]*d(\d+)"\s+d="([^"]+)"', svg_content)

    # 2. 붓 진행 중심선 추출 (clip-path)
    medial_matches = re.findall(rf'clip-path="url\(#z{codepoint}c(\d+)\)"\s+d="([^"]+)"', svg_content)
    if not medial_matches:
        medial_matches = re.findall(r'clip-path="[^"]*c(\d+)"\s+d="([^"]+)"', svg_content)

    outlines = {int(m[0]): m[1] for m in outline_matches}
    medials = {int(m[0]): m[1] for m in medial_matches}
    total_strokes = len(outlines)

    char_svg_dir = os.path.join(SVG_HANZI_DIR, f"char_{char}")
    os.makedirs(char_svg_dir, exist_ok=True)

    # 전체 완성 글자 SVG
    full_svg_path = os.path.join(char_svg_dir, "full.svg")
    paths_xml = "\n".join([f'  <path d="{d}" fill="#FFD166"/>' for d in outlines.values()])
    with open(full_svg_path, "w", encoding="utf-8") as f:
        f.write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <path d="M 0 0 L 1 1 M 1024 0 L 1023 1 M 0 1024 L 1 1023 M 1024 1024 L 1023 1023" fill="none" stroke="#000000" stroke-width="0.01" opacity="0.01"/>
{paths_xml}
</svg>''')

    strokes_data = []
    for order in range(1, total_strokes + 1):
        outline_d = outlines.get(order, "")
        medial_d = medials.get(order, "")

        # 획 윤곽선 SVG
        stroke_svg_path = os.path.join(char_svg_dir, f"stroke_{order}.svg")
        with open(stroke_svg_path, "w", encoding="utf-8") as f:
            f.write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <path d="M 0 0 L 1 1 M 1024 0 L 1023 1 M 0 1024 L 1 1023 M 1024 1024 L 1023 1023" fill="none" stroke="#000000" stroke-width="0.01" opacity="0.01"/>
  <path d="{outline_d}" fill="#FFD166"/>
</svg>''')

        # 붓 진행 중심선 SVG (붓촉 이동 가이드)
        medial_svg_path = os.path.join(char_svg_dir, f"medial_{order}.svg")
        if medial_d:
            with open(medial_svg_path, "w", encoding="utf-8") as f:
                f.write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <path d="M 0 0 L 1 1 M 1024 0 L 1023 1 M 0 1024 L 1 1023 M 1024 1024 L 1023 1023" fill="none" stroke="#000000" stroke-width="0.01" opacity="0.01"/>
  <path d="{medial_d}" fill="none" stroke="#F59E0B" stroke-width="48" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''')

        strokes_data.append({
            "order": order,
            "outline_d": outline_d,
            "medial_d": medial_d,
            "stroke_svg_path": stroke_svg_path,
            "medial_svg_path": medial_svg_path if medial_d else None
        })

    return {
        "char": char,
        "stroke_count": total_strokes,
        "full_svg_path": full_svg_path,
        "strokes": strokes_data
    }
