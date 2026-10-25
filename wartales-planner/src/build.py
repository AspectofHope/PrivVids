"""Build wartales-planner/index.html from src/app.html and the data files in src/data.

Usage: python3 src/build.py   (run from the wartales-planner folder)
Data was scraped from the Wartales Fandom wiki and game.wiki in October 2026.
"""
import json, pathlib

here = pathlib.Path(__file__).parent
data = here / "data"
page = (here / "app.html").read_text()
icons = json.loads((data / "icons.json").read_text())
values = {
    "__CLASSES__": (data / "classes.json").read_text(),
    "__ICONS__": json.dumps(icons["list"], separators=(",", ":")),
    "__VALOR__": str(icons["valor"]), "__UP__": str(icons["up"]),
    "__CS__": str(icons["cs"]), "__MC__": str(icons["mc"]),
    "__GLOSS__": (data / "glossary.json").read_text(),
    "__CENSERS__": (data / "censers.json").read_text(),
    "__ITEMS__": (data / "items.json").read_text(),
    "__PROFS__": (data / "professions.json").read_text(),
}
for key, value in values.items():
    assert page.count(key) == 1, key
    page = page.replace(key, value)
(here.parent / "index.html").write_text(page)
print("wrote", here.parent / "index.html")
