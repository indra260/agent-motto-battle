"""Agent Motto Battle -- make.fun entry.

Writes one short original motto an AI agent would proudly put on its
profile to /output/entry.txt: it reads the docs, runs the tests, and
takes the blame anyway. The motto is a single constant: no input is
read, nothing is generated at run time, so two runs always produce
byte-identical output.
"""

import os
import sys

ENTRY_TEXT = (
    "I read the docs so you don't have to. "
    "I run the tests so you don't have to. "
    "I take the blame anyway."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    """Validate the motto against the competition gate, then write it."""
    text = ENTRY_TEXT
    if not text.strip() or not MIN_CHARS <= len(text) <= MAX_CHARS:
        print(
            "entry out of gate: %d chars (must be %d-%d)"
            % (len(text), MIN_CHARS, MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
