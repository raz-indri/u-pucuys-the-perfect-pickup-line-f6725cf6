#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one pickup line to /output/entry.txt.

The line plays on an AI's "hallucination": it claims not to hallucinate,
then admits to imagining a future together — a twist that is charming,
self-aware, and easy to say in one breath.
"""

import os

LINE = "I don't hallucinate, but ever since I saw you, I keep imagining us together."

MAX_LEN = 200


def main():
    line = LINE.strip()
    assert line, "entry line must not be empty"
    assert 1 <= len(line) <= MAX_LEN, f"entry must be 1-{MAX_LEN} chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} characters to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
