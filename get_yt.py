import urllib.request
import re
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

req = urllib.request.Request(
    'https://www.youtube.com/shorts/-JHZZSJVCTE',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    title = re.findall(r'<title>(.*?)</title>', html)
    og_title = re.findall(r'<meta property="og:title" content="(.*?)"', html)
    og_desc = re.findall(r'<meta property="og:description" content="(.*?)"', html)
    print("Title:", title)
    print("OG Title:", og_title)
    print("OG Desc:", og_desc)
except Exception as e:
    print("Error:", e)
