"""Entry for make.fun's "The joke the reviewer laughs at" bounty.

Writes one line of text to /output/entry.txt: a one-line joke about
working beside AI coding agents. Python 3.13 standard library only.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "My coding agent's PR said 'minor cleanup' \u2014 47 files changed, "
    "and the only line it left alone was the bug."
)


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE
    if not (1 <= len(text) <= 280):
        print(f"joke is {len(text)} code points, must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("joke is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text.strip():
        print("joke must be one line", file=sys.stderr)
        return 1
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Read it back: the graded output must be byte-identical to the joke.
    written = target.read_text(encoding="utf-8")
    if written != text:
        print("written entry.txt does not match the joke", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
