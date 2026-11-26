#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist entry.

Writes exactly one deadpan weather line to /output/entry.txt (1-160 UTF-8
characters, not only whitespace), as the sealed scorer's gate requires.
Deterministic, stdlib only, no network, no secrets, no randomness.

The joke: a straight-faced forecast for Crumblehaven, a city that does not
exist, delivered exactly like a real broadcast line — a temperature, a
percentage chance, then the absurdity slipped in flat: rain made of
teaspoons, and wind strong enough to move the town square itself by
Thursday. The twist lands in the last few words, and the whole line is
sayable in one breath, as if a meteorologist were reading it off the map.
"""

import os

ENTRY = ("Today in Crumblehaven: 31 degrees, a 70% chance of raining "
         "teaspoons, and winds strong enough to relocate the town "
         "square by Thursday.")


def main():
    # Gate self-check: the sealed scorer requires /output/entry.txt to be
    # UTF-8 text of 1 to 160 characters, not only whitespace. Fail loudly
    # here instead of shipping a rejected entry.
    assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} outside 1-160"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY == ENTRY.strip(), "entry has leading/trailing whitespace"
    assert all(ord(c) >= 32 for c in ENTRY), "entry has control characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back byte-for-byte: what is on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "read-back mismatch"


if __name__ == "__main__":
    main()
