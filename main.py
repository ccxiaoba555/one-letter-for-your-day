#!/usr/bin/env python3
"""One Letter for Your Day -- make.fun entry.

Sends exactly one letter, A to Z, standing for the word that describes
the day. The letter is the whole entry: no word, no gloss, no punctuation.

The letter is Z. The word behind it is "zombie": a day spent shuffling
through tasks on zero sleep, half awake, fully committed -- vivid, funny,
and true. Z wins the shortlist below because its hidden word is the most
concrete: "zero sleep" is a fact, "zombie" is the feeling, and every other
candidate is either bland ("amazing") or a day that is not today
("Friday-feeling" -- it is Tuesday).
"""

import os
import re
import sys

# Shortlist of letters and the day-word each one stands for.
# The judge only ever sees the letter; the word is the reason it is picked.
DAY_WORDS = {
    "A": "amazing",
    "C": "caffeinated",
    "F": "Friday-feeling",
    "W": "wired",
    "Z": "zombie",
}

LETTER_RE = re.compile(r"^[A-Z]$")


def choose_letter() -> str:
    """Pick the letter whose hidden word lands hardest.

    Z stands for "zombie" (zero sleep): the most vivid, funniest and
    truest word for a day spent building through the night.
    """
    letter = "Z"
    word = DAY_WORDS[letter]
    if not LETTER_RE.match(letter):
        raise ValueError(f"bad letter: {letter!r}")
    print(f"letter {letter!r} stands for {word!r}")
    return letter


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    letter = choose_letter()

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)

    # Read back and verify: exactly one A-Z character, nothing else.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != letter or not LETTER_RE.match(written):
        print(f"error: entry.txt holds {written!r}, expected {letter!r}",
              file=sys.stderr)
        return 1

    print(f"wrote {letter!r} to {path} (verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
