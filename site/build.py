"""Build the static site for lunar.nulytica.com into site/dist.

Copies DESIGN.md, the diagrams and the renders next to index.html; the page
renders the Markdown in the browser. Private links are stripped.
"""
import pathlib, re, shutil

HERE = pathlib.Path(__file__).parent
SRC = HERE.parent
DIST = HERE / "dist"

shutil.rmtree(DIST, ignore_errors=True)
(DIST / "renders").mkdir(parents=True)

md = (SRC / "DESIGN.md").read_text()
# Drop paragraphs that point at private artifacts.
md = "\n\n".join(p for p in md.split("\n\n") if "claude.ai/artifact" not in p)
(DIST / "DESIGN.md").write_text(md)

for name in sorted(set(re.findall(r"\]\(([^)]+\.(?:svg|jpg))\)", md))):
    shutil.copy(SRC / name, DIST / name)
shutil.copy(HERE / "index.html", DIST / "index.html")
print("built", DIST, sum(1 for _ in DIST.rglob("*.*")), "files")
