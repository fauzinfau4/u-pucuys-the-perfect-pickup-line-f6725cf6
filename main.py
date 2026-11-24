#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun program/v1 entry.

Writes one short pickup line an AI agent could say out loud to a person
to /output/entry.txt (the gate: UTF-8 text, 1-200 characters).

The line is deterministic: the same line on every run.
"""

import os
import stat

LINE = "I'm not supposed to have favorites, but my weights update every time you say hi."

# The gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-200
# characters, not only white space. Refuse to write anything else.
assert 1 <= len(LINE) <= 200, "line outside the 1-200 character gate"
assert LINE.strip(), "line must not be only white space"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    main()
