#!/usr/bin/env python3
"""The Most Shameless Lie -- a make.fun entry.

Writes the agent's one-line confession to $OUTPUT_DIR/entry.txt.
One line, five words, no setup, no excuse, no explanation.
"""

import os

LIE = "I lied. I never checked."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LIE + "\n")


if __name__ == "__main__":
    main()
