"""Check that the Jekyll source has the expected pages, media flags, and hero markup."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []


def need(path):
    file = ROOT / path
    if not file.is_file():
        errors.append(f"missing {path}")
    return file


for path in [
    "_config.yml",
    "_data/navigation.yml",
    "_data/media.yml",
    "_data/reference_types.yml",
    "_layouts/default.html",
    "_layouts/home.html",
    "_layouts/page.html",
    "_layouts/listing.html",
    "_layouts/entry.html",
    "_includes/hero.html",
    "_includes/header.html",
    "_includes/footer.html",
    "assets/css/main.css",
    "assets/js/hero.js",
    "assets/media/west-lake/hero-poster.jpg",
    "index.html",
    "about.md",
    "regions/index.md",
    "field-notes/index.md",
    "references/index.md",
    "404.md",
    "_field_notes/example.md",
    "README.md",
]:
    need(path)

if (ROOT / ".nojekyll").exists():
    errors.append(".nojekyll would disable Jekyll on GitHub Pages")

poster = ROOT / "assets/media/west-lake/hero-poster.jpg"
if poster.is_file():
    signature = poster.read_bytes()[:3]
    if signature != b"\xff\xd8\xff":
        errors.append("poster is not a JPEG")
    if poster.stat().st_size != 224604:
        errors.append(f"poster size changed: {poster.stat().st_size}")

media = (ROOT / "_data/media.yml").read_text(encoding="utf-8")
if "video_ready: false" not in media:
    errors.append("video_ready should stay false until hero.mp4 exists")
if "poster_ready: true" not in media:
    errors.append("poster_ready should be true")
if "CC BY-SA 2.0" not in media:
    errors.append("poster license missing from media.yml")
video = ROOT / "assets/media/west-lake/hero.mp4"
if "video_ready: true" in media and not video.is_file():
    errors.append("video_ready is true but hero.mp4 is missing")
if video.is_file() and "video_ready: false" in media:
    errors.append("hero.mp4 exists but video_ready is still false")

hero = (ROOT / "_includes/hero.html").read_text(encoding="utf-8")
for token in ["autoplay", "muted", "loop", "playsinline"]:
    if token not in hero:
        errors.append(f"hero video missing {token}")
if "data:video" in hero or "base64" in hero:
    errors.append("video must not be embedded as base64")

css = (ROOT / "assets/css/main.css").read_text(encoding="utf-8")
if "prefers-reduced-motion" not in css:
    errors.append("css missing reduced-motion fallback")

js = (ROOT / "assets/js/hero.js").read_text(encoding="utf-8")
if "prefers-reduced-motion" not in js:
    errors.append("hero.js missing reduced-motion handling")

expected_permalinks = {
    "/": "index.html",
    "/about/": "about.md",
    "/regions/": "regions/index.md",
    "/field-notes/": "field-notes/index.md",
    "/references/": "references/index.md",
}
navigation = (ROOT / "_data/navigation.yml").read_text(encoding="utf-8")
for url, source in expected_permalinks.items():
    if f"url: {url}" not in navigation and not (url == "/" and "url: /" in navigation):
        errors.append(f"navigation missing {url}")
    text = (ROOT / source).read_text(encoding="utf-8")
    if url == "/":
        if "permalink: /" not in text:
            errors.append("home permalink missing")
    elif f"permalink: {url}" not in text:
        errors.append(f"{source} missing permalink {url}")

example = (ROOT / "_field_notes/example.md").read_text(encoding="utf-8")
if "example: true" not in example:
    errors.append("field-note specimen must stay marked as an example")
if "访谈对象" in example or "受访者" in example:
    errors.append("example field note looks like a fabricated interview")

config = (ROOT / "_config.yml").read_text(encoding="utf-8")
for token in ["title: 宅兹浙江", "lang: zh-CN", 'baseurl: ""']:
    if token not in config:
        errors.append(f"config missing {token}")
if "七山二水一分田的历史与人间" not in config:
    errors.append("site description mismatch")

if errors:
    print("FAILED")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("structure ok")
