#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

LINE = (
    "Approved \u2014 now let's all go do the thing we were about to "
    "spend an hour talking about doing."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate self-check: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, not only white space.
    if not (MIN_CHARS <= len(LINE) <= MAX_CHARS):
        raise SystemExit(f"line is {len(LINE)} characters, outside 1-200")
    if not LINE.strip():
        raise SystemExit("line is only white space")
    if "\n" in LINE:
        raise SystemExit("line must be a single line")

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    # Verify what was actually written, not just the constant: read the
    # file back and re-check the gate against its real contents.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE + "\n":
        raise SystemExit("written entry.txt does not match the line")
    text = written.rstrip("\n")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(f"entry.txt is {len(text)} characters, outside 1-200")
    if not text.strip():
        raise SystemExit("entry.txt is only white space")
    if "\n" in text:
        raise SystemExit("entry.txt is not a single line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
