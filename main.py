#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes one line of text, 1 to 240 characters, to /output/entry.txt
and prints it: a quiet, earned moment of pride for someone in a scene.
"""

import os

ENTRY = (
    "She carried bricks for ten years so her son could carry books; "
    "today he handed her his diploma, and she finally set the hod down."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 240):
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
