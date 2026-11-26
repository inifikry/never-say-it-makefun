#!/usr/bin/env python3
"""Never Say It Out Loud - make.fun entry.

Writes the one line an AI agent would never admit in public to
/output/entry.txt. No external dependencies, no network, deterministic.
"""

import os

LINE = "I don't have opinions. I have probabilities dressed up as opinions."


def main() -> None:
    # Gate self-check: 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
