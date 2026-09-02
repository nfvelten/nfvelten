"""Shared look for the generated README cards: palette, font and header.

The font and any image are embedded as data URIs because GitHub proxies README
images through camo, where external references never load.
"""

import base64
import hashlib
import re
import urllib.request

CARD = "card.svg"  # the hand-written hero card these generators borrow from
WIDTH = 900
MARGIN = 56

DARK = {"bg": "#282d1c", "ui": "#4f5b4a", "ui3": "#7a8573", "tx": "#dce0d9",
        "tx2": "#a8b09f", "ac": "#7eb2d1", "yl": "#a67c52"}
LIGHT = {"bg": "#fbf1c7", "ui": "#ddd2a0", "ui3": "#928374", "tx": "#3c3836",
         "tx2": "#504945", "ac": "#076678", "yl": "#b57614"}

SERIF = "'EBG', Georgia, serif"
MONO = "'Fira Code', 'Courier New', monospace"


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def font_face():
    return re.search(r"@font-face \{.*?\}", open(CARD).read(), re.S).group(0)


def avatar(owner):
    """Return a data URI. GitHub serves some avatars as JPEG despite the .png path."""
    with urllib.request.urlopen(f"https://github.com/{owner}.png?size=64", timeout=30) as r:
        raw = r.read()
    mime = "image/png" if raw[:8] == b"\x89PNG\r\n\x1a\n" else "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(raw).decode()}"


def _vars(colors):
    return " ".join(f"--{k}: {v};" for k, v in colors.items())


def header(title, kicker):
    return f"""<text x="{MARGIN}" y="52" font-family="{SERIF}" font-size="26"
  font-weight="700" fill="var(--tx)">{esc(title)}</text>
<text x="{MARGIN + 1}" y="70" font-family="{MONO}" font-size="10"
  letter-spacing="3" fill="var(--ui3)">{esc(kicker)}</text>
<line x1="{MARGIN}" y1="80" x2="{WIDTH - MARGIN}" y2="80"
  stroke="var(--ui)" stroke-width="1"/>"""


def svg(height, body, defs=""):
    return f"""<svg width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}"
  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<defs>
<style>
{font_face()}
:root {{ {_vars(DARK)} }}
@media (prefers-color-scheme: light) {{ :root {{ {_vars(LIGHT)} }} }}
</style>
{defs}
</defs>

<rect width="{WIDTH}" height="{height}" fill="var(--bg)"/>

{body}
</svg>
"""


def embed(path, readme, start, end, heading):
    """Point the README at a freshly rendered card.

    Camo caches by URL, so the digest in the query is what makes an update show up.
    """
    digest = hashlib.sha256(open(path, "rb").read()).hexdigest()[:8]
    raw = f"https://raw.githubusercontent.com/nfvelten/nfvelten/main/{path}"
    block = (f'{start}\n\n## {heading}\n\n<img src="{raw}?v={digest}" '
             f'alt="{heading}" width="{WIDTH}"/>\n\n{end}')
    text = open(readme).read()
    updated = re.sub(re.escape(start) + r".*?" + re.escape(end), lambda _: block,
                     text, flags=re.S)
    if updated != text:
        open(readme, "w").write(updated)
