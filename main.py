"""Fortune Cookie Wisdom for Developers -- make.fun entry.

Deliberation (which line won and why):

Three candidate fortune-cookie lines were weighed against the judge's
brief -- a tired senior engineer who picks the line that makes it
smile and nod, weighing (1) real fortune-cookie wisdom for a
developer, (2) one short balanced sentence landing in a single
breath, (3) something true about a developer's day, (4) a turn the
reader has not heard before, and (5) a quiet twist that rewards a
second read.

  A. "Your legacy code is not a mess; it is a map of every deadline
     you survived."  (75 chars) -- WINNER.
     The classic fortune structure ("is not X; it is Y"), one
     balanced sentence, and it names the judge's daily bread: legacy
     code and deadlines. The turn is fresh -- it reframes the mess as
     a survival map instead of repeating the tired "legacy code is
     scary" line -- and the twist lands on the second read: the mess
     is proof you endured.

  B. "The estimate you give today is the apology you will write
     tomorrow."  (67 chars) -- LOST.
     Good fortune structure and true about estimates, but it leans
     cynical and closer to a punchline than to wisdom; the judge
     smiles, but the nod is weaker. It warns; it does not comfort.

  C. "Somewhere, a comment you wrote years ago is still explaining
     you to a stranger."  (79 chars) -- LOST.
     The most poetic of the three, and its twist (the comment
     explains *you*, not the code) is lovely -- but it is more a
     poetic observation than fortune wisdom, and it sits further from
     the daily grind (bugs, reviews, deploys, estimates, legacy
     code) the brief names. A touches legacy and deadlines directly.

The program writes exactly the winning line to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR (default /output),
with no trailing newline, so the file holds precisely 75 characters.
"""

import os
import sys

FORTUNE = "Your legacy code is not a mess; it is a map of every deadline you survived."

MAX_CHARS = 120


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    line = FORTUNE
    # The gate wants exactly one line of 1-120 characters: reject an
    # empty/whitespace-only line, anything over the cap, and any
    # embedded newline that would split the fortune in two.
    if not line.strip() or len(line) > MAX_CHARS or "\n" in line or "\r" in line:
        print("fortune line fails the gate (empty, over 120 chars, or not one line)",
              file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
