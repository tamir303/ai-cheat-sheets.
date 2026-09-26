# render_sheet.py STUDIO_INDEX_HTML SHEET_DOC_JSON OUT_PNG [SCALE] [FONTS_DIR]
# Renders one cheat-sheet record with Cheat Sheet Studio's own renderer and saves a PNG.
import json, os, sys
from playwright.sync_api import sync_playwright
page_file, doc_file, out = sys.argv[1], sys.argv[2], sys.argv[3]
scale = float(sys.argv[4]) if len(sys.argv) > 4 else 2
F = (sys.argv[5] if len(sys.argv) > 5 else "fonts") + "/node_modules/@fontsource"
F = os.path.abspath(F)
faces = "<style>" + "".join(
    f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{F}/{pkg}/files/{pkg}-latin-{w}-normal.woff2')}}"
    for fam, pkg, ws in [("Kalam", "kalam", (400, 700)), ("Patrick Hand", "patrick-hand", (400,)), ("Nunito", "nunito", (400, 600, 700, 800))]
    for w in ws) + "</style>"
doc = json.load(open(doc_file))
stub = """<script>
const DOC = %s;
const snap = () => ({docs:[{id:'sheet', exists:true, data:()=>DOC}], size:1, empty:false});
const db = { doc: () => ({get: async()=>({exists:false}), set: async()=>{}, delete: async()=>{}}),
  collection: () => { const q = {orderBy:()=>q, limit:()=>q, onSnapshot:(f)=>{ setTimeout(()=>f(snap()),0); return ()=>{}; }, doc:()=>db.doc()}; return q; } };
window.claude = { use: async (n) => n === 'db' ? db : null };
</script>""" % json.dumps(doc).replace("</", "<\\/")
html = open(page_file).read().replace("<head>", "<head>" + faces + stub, 1)
tmp = os.path.abspath(out) + ".render.html"
open(tmp, "w").write(html)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=scale)
    pg.goto("file://" + tmp); pg.wait_for_timeout(900)
    pg.click(".lib-item[data-lib='sheet']"); pg.wait_for_timeout(300)
    pg.click("#size-btn"); pg.wait_for_timeout(700)
    info = pg.evaluate("""() => ({
      diagrams: [...document.querySelectorAll('#stage .cs-diag')].map(s => s.textContent.includes('didn’t draw') ? 'failed' : 'ok'),
      height: document.querySelector('#stage .cs').offsetHeight })""")
    pg.locator("#stage .cs").screenshot(path=out)
    b.close()
os.remove(tmp)
print(json.dumps(info))
