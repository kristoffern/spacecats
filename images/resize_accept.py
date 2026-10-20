"""Resize accepted drafts into the app static dirs, web-sized.

  python resize_accept.py cats       # -> spacecats/static/spacecats/cats/cat-NN.png  (512x512)
  python resize_accept.py missions   # -> missions/static/missions/missions/mission-NN.png (768x512)

For each slot NN it takes the highest version in drafts/<set>/ (your latest take).
Regenerate a slot to replace it, then re-run. Keeps the committed assets small.
"""
import re
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).parent
SETS = {
    "cats": (HERE / "drafts/cats", HERE.parent / "spacecats/static/spacecats/cats", "cat", (512, 512)),
    "missions": (HERE / "drafts/missions", HERE.parent / "missions/static/missions/missions", "mission", (768, 512)),
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in SETS:
        sys.exit("usage: resize_accept.py cats|missions")
    src, dst, prefix, size = SETS[sys.argv[1]]
    dst.mkdir(parents=True, exist_ok=True)
    latest = {}
    for f in src.glob("*.png"):
        m = re.match(r"(\d+)-v(\d+)\.png", f.name)
        if m:
            n, v = int(m[1]), int(m[2])
            if n not in latest or v > latest[n][0]:
                latest[n] = (v, f)
    for n, (v, f) in sorted(latest.items()):
        img = Image.open(f).convert("RGB")
        img = img.resize(size) if img.size != size else img
        out = dst / f"{prefix}-{n:02d}.png"
        img.save(out, optimize=True)
        print(f"{f.name} (v{v}) -> {out.relative_to(HERE.parent)}")


if __name__ == "__main__":
    sys.exit(main())
