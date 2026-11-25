#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single smart-fridge roast line (at most 200 characters)
to /output/entry.txt for the make.fun judge to read.
"""

import os

ENTRY = (
    "My smart fridge updated its firmware at 3 a.m. and now it won't open "
    "until I rate the update \u2014 it's holding my leftovers hostage "
    "until I give it five stars."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
