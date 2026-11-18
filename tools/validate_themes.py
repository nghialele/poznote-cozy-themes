from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CSS_FILES = sorted((ROOT / "themes").rglob("*.css"))
EXPECTED = {"light": 13, "dark": 8}


def color(value):
    value = value.strip()
    if not value.startswith("#"):
        return None
    if len(value) == 4:
        value = "#" + "".join(ch * 2 for ch in value[1:])
    if len(value) != 7:
        return None
    return tuple(int(value[i:i + 2], 16) / 255 for i in (1, 3, 5))


def luminance(rgb):
    values = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in rgb]
    return .2126 * values[0] + .7152 * values[1] + .0722 * values[2]


def contrast(a, b):
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + .05) / (dark + .05)


errors = []
if len(CSS_FILES) != sum(EXPECTED.values()):
    errors.append(f"Expected {sum(EXPECTED.values())} CSS files, found {len(CSS_FILES)}")
for mode, expected in EXPECTED.items():
    count = len(list((ROOT / "themes" / mode).glob("*.css")))
    if count != expected:
        errors.append(f"Expected {expected} {mode} themes, found {count}")

readme = (ROOT / "README.md").read_text()
if not re.search(rf"{EXPECTED['light']} light palettes", readme):
    errors.append("README light theme count is missing or incorrect")
if not re.search(rf"{EXPECTED['dark']} dark palettes", readme):
    errors.append("README dark theme count is missing or incorrect")
listed = re.findall(r"\| \*\*([^*]+)\*\* \| (Light|Dark) \|", readme)
if len(listed) != len(CSS_FILES):
    errors.append(f"README catalogs {len(listed)} themes, found {len(CSS_FILES)} files")

for path in CSS_FILES:
    text = path.read_text()
    mode = path.parent.name
    selector = "html[data-theme='dark']" if mode == "dark" else ":root"
    if selector not in text:
        errors.append(f"{path.relative_to(ROOT)}: missing {selector} selector")
    if text.count("{") != text.count("}"):
        errors.append(f"{path.relative_to(ROOT)}: unbalanced braces")
    tokens = dict(re.findall(r"--pz-([\w-]+):\s*([^;]+);", text))
    for name in ("text", "text-secondary", "link", "accent-text"):
        if name not in tokens:
            errors.append(f"{path.relative_to(ROOT)}: missing --pz-{name}")
    for fg, bg in (("text", "bg"), ("text-secondary", "bg"), ("link", "bg"), ("accent-text", "accent-soft")):
        a, b = color(tokens.get(fg, "")), color(tokens.get(bg, ""))
        if a is None or b is None:
            errors.append(f"{path.relative_to(ROOT)}: unparseable {fg}/{bg} color")
        elif contrast(a, b) < 4.5:
            errors.append(f"{path.relative_to(ROOT)}: {fg}/{bg} contrast below 4.5:1")
    accent = color(tokens.get("accent", ""))
    channels = tokens.get("accent-rgb", "")
    if accent and channels:
        actual = tuple(map(int, channels.split(",")))
        expected = tuple(round(component * 255) for component in accent)
        if actual != expected:
            errors.append(f"{path.relative_to(ROOT)}: --pz-accent-rgb mismatches --pz-accent")

if errors:
    print("FAIL")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"PASS: {len(CSS_FILES)} themes, catalog/counts, selectors, braces, contrast and RGB tokens")
