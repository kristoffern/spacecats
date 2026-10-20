"""Generate spacecats demo images through the OpenAI image API, into drafts/.

Adapted from the botanical-plates generate.py pattern. Two prompt sets, each a
locked STYLE block (for consistency) plus one Subject per slot:
  prompts_cats.org     -> anthropomorphic uniformed crew-cat headshots
  prompts_missions.org -> deep-space mission scenes

Usage:
  python generate.py --list-models
  python generate.py cats 1 2 3
  python generate.py missions 1-25
  python generate.py cats all --pause 20

- The prompt sent = the file's STYLE block + the slot's Subject, so every image in a
  set shares style, palette and framing and only the subject changes.
- Key from ~/.config/openai/api-key (chmod 600), never from the command line.
- Never overwrites: writes drafts/<set>/NN-vK.png with the next free K, so you can
  regenerate a slot and keep the old take to compare on a contact sheet.
- Run this on Tinseltown (where openai + the key live), not on the demo box.
"""
import argparse
import base64
import re
import sys
import time
from pathlib import Path

from openai import OpenAI

HERE = Path(__file__).parent
KEY = Path.home() / ".config" / "openai" / "api-key"


def style_and_slots(category):
    text = (HERE / f"prompts_{category}.org").read_text()
    style = re.search(r"#\+begin_style\n(.*?)\n#\+end_style", text, re.S)
    style = style[1].strip() if style else ""
    slots = {}
    for m in re.finditer(r"^\* (\d+)\. (.+?)\n(.*?)(?=^\* |\Z)", text, re.S | re.M):
        n, title, body = int(m[1]), m[2].strip(), m[3]
        block = re.search(r"#\+begin_example\n(.*?)\n#\+end_example", body, re.S)
        slots[n] = dict(title=title, subject=block[1].strip() if block else None)
    return style, slots


def parse_slots(args, available):
    if not args or "all" in args:
        return sorted(available)
    nums = []
    for a in args:
        if "-" in a:
            lo, hi = a.split("-")
            nums += list(range(int(lo), int(hi) + 1))
        else:
            nums.append(int(a))
    return nums


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("category", nargs="?", choices=["cats", "missions"])
    ap.add_argument("slots", nargs="*")
    ap.add_argument("--model", default="gpt-image-2")
    ap.add_argument("--size", default=None)
    ap.add_argument("--quality", default="high")
    ap.add_argument("--pause", type=int, default=20)
    ap.add_argument("--list-models", action="store_true")
    a = ap.parse_args()

    client = OpenAI(api_key=KEY.read_text().strip(), base_url="https://api.openai.com/v1")
    models = sorted(m.id for m in client.models.list() if m.id.startswith("gpt-image"))
    if a.list_models or not a.category:
        print("gpt-image models available:", models or "NONE")
        return
    if a.model not in models:
        sys.exit(f"model {a.model} not available to this key: {models}")

    style, slots = style_and_slots(a.category)
    want = parse_slots(a.slots, slots)
    size = a.size or ("1024x1024" if a.category == "cats" else "1536x1024")
    outdir = HERE / "drafts" / a.category
    outdir.mkdir(parents=True, exist_ok=True)
    print(f"{a.category}: model {a.model}, size {size}, quality {a.quality}, {len(want)} image(s)")

    for i, n in enumerate(want):
        s = slots.get(n)
        if not s or not s["subject"]:
            print(f"#{n}: no subject, skipped")
            continue
        prompt = f"{style}\n\nSubject: {s['subject']}"
        base = f"{n:02d}-v"
        k = 1
        while (outdir / f"{base}{k}.png").exists():
            k += 1
        path = outdir / f"{base}{k}.png"
        print(f"#{n} {s['title']} ...", flush=True)
        t = time.time()
        for attempt in (1, 2):
            try:
                r = client.images.generate(model=a.model, prompt=prompt, size=size, quality=a.quality)
                path.write_bytes(base64.b64decode(r.data[0].b64_json))
                print(f"   -> {path.name} ({time.time() - t:.0f}s)", flush=True)
                break
            except Exception as e:
                print(f"   ! attempt {attempt}: {type(e).__name__}: {str(e)[:120]}", flush=True)
                if attempt == 2:
                    print(f"   #{n} SKIPPED", flush=True)
                else:
                    time.sleep(5)
        if i < len(want) - 1:
            time.sleep(a.pause)


if __name__ == "__main__":
    sys.exit(main())
