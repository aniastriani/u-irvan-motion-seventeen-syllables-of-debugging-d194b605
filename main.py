#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5, seventeen syllables) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library.
"""

import os

HAIKU = (
    "Midnight cursor blinks\n"          # 5 syllables
    "the log line lies, then comes clean\n"  # 7 syllables
    "it was my typo\n"                 # 5 syllables
)


def main() -> None:
    # The gate wants UTF-8 text of 1 to 200 characters, not only whitespace.
    text = HAIKU.strip("\n")
    assert 1 <= len(text) <= 200, "haiku must be 1-200 characters"
    assert text.count("\n") == 2, "haiku must be exactly three lines"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
