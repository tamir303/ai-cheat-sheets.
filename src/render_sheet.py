"""Render one cheat sheet to PNG.

Usage: python src/render_sheet.py SHEET_JSON OUT_PNG [SCALE] [FONTS_DIR]

SHEET_JSON is a record {title, concept, data}. FONTS_DIR holds the npm packages
@fontsource/kalam, @fontsource/nunito and @fontsource/patrick-hand.
"""
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
FACES = [("Kalam", "kalam", (400, 700)), ("Patrick Hand", "patrick-hand", (400,)), ("Nunito", "nunito", (400, 600, 700, 800))]

doc_file, out = Path(sys.argv[1]), Path(sys.argv[2]).resolve()
scale = float(sys.argv[3]) if len(sys.argv) > 3 else 1.5
fonts = Path(sys.argv[4] if len(sys.argv) > 4 else "fonts").resolve() / "node_modules" / "@fontsource"

faces = "".join(
    f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('{(fonts / pkg / 'files' / f'{pkg}-latin-{w}-normal.woff2').as_uri()}')}}"
    for fam, pkg, weights in FACES for w in weights)
doc = json.dumps(json.loads(doc_file.read_text())).replace("</", "<\\/")
inject = f"<style>{faces}</style><script>window.DOC = {doc};</script>"
html = (HERE / "sheet.html").read_text().replace("<head>", "<head>" + inject, 1)

tmp = out.with_suffix(".render.html")
tmp.write_text(html)
try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=scale)
        page.goto(tmp.as_uri())
        page.wait_for_function("window.RENDERED === true", timeout=30000)
        page.wait_for_timeout(300)
        info = page.evaluate("""() => ({
          diagrams: [...document.querySelectorAll('.cs-diag')].map(s => s.textContent.includes('didn’t draw') ? 'failed' : 'ok'),
          height: document.querySelector('.cs').offsetHeight })""")
        page.locator(".cs").screenshot(path=str(out))
        browser.close()
finally:
    tmp.unlink(missing_ok=True)
print(json.dumps(info))
