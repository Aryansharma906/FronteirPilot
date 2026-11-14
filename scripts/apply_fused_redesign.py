import re
from pathlib import Path

ROOT = Path("/Users/aryansharma/Desktop/linkedin-skills-main")
TARGET_HTML = ROOT / "studio" / "templates" / "frontierpilot.html"
DOCS_HTML = ROOT / "docs" / "frontierpilot.html"

print("Reading", TARGET_HTML)
content = TARGET_HTML.read_text(encoding="utf-8")
print(f"Current content size: {len(content)} bytes")

