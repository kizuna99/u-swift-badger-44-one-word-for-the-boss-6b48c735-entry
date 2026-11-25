# SPDX-License-Identifier: MIT
"""One Word for the Boss — writes the single entry word to /output/entry.txt."""
import os

WORD = "Glorygoblin"


def main() -> None:
    # The gate counts 1-30 UTF-8 characters, not only whitespace: the word
    # is written exactly, with no trailing newline or extra text.
    assert 1 <= len(WORD) <= 30 and WORD.strip() == WORD and " " not in WORD
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
