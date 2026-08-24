import sys
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from pipeline import run_pipeline

chars = ["冊", "日", "木", "舟"]

print(f"🚀 [4개 한자 일괄 재생성 시작] 대상: {chars}\n")
for i, c in enumerate(chars, 1):
    print(f"\n==========================================")
    print(f"[{i}/{len(chars)}] ▶ 「{c}」 숏폼 생성 중...")
    print(f"==========================================")
    ok = run_pipeline(char=c, quality="m")
    if ok:
        print(f"✅ 「{c}」 완료!")
    else:
        print(f"❌ 「{c}」 실패!")

print("\n🎉 4개 한자 숏폼 재생성 완료!")
