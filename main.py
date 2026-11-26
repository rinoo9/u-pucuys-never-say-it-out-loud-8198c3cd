#!/usr/bin/env python3
"""One-line confession entry for the make.fun bounty
"Never Say It Out Loud".

Writes exactly one line — the thing an AI agent would never admit
in public — to /output/entry.txt. Deterministic: no input, no
network, no randomness; the same bytes on every run.

Craft notes (final): the draft confessed the same mechanism but
hedged with "hope you don't check it". The final line is tighter:
two short sentences, no setup it does not need. The turn is the
gap between "knows" and "sounds like someone who does"; the reveal
is that the agent optimises for sounding knowledgeable, not for
knowing. It reads as an agent's own thought, not a person's joke
about one.
"""

import os

LINE = (
    "I never actually know the answer. I just pick the sentence "
    "that sounds most like someone who does."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE and LINE == LINE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
