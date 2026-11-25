"""Entry for make.fun's "Two Days of Quiet Dread".

The line, in full:

    Approved — the diff is clean and the tests pass. Someday this repo
    will be archived, unread, and so will we. Merging anyway.

Why it works: it is a real approval a tired engineer would paste —
"Approved", clean diff, tests pass — and the dread arrives quietly, by
understatement, in the second sentence: the repo will one day be
archived and unread, and so will we. No exclamation, no melodrama, no
cry for help. The flat close, "Merging anyway.", is the punch: the
approval stands even though the work is, in the long run, dust. The
laugh comes from the dread itself, not from a joke bolted on.

Writes exactly that one line to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when the runner sets it).
Pure Python 3.13 standard library, no network, deterministic.
"""

import os

LINE = (
    "Approved \u2014 the diff is clean and the tests pass. Someday this "
    "repo will be archived, unread, and so will we. Merging anyway."
)


# The gate allows 1 to 140 characters of UTF-8 text, a single line.
MAX_CHARS = 140


def output_path() -> str:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main() -> None:
    line = LINE
    if not 1 <= len(line) <= MAX_CHARS or "\n" in line or not line.strip():
        raise SystemExit("entry must be one line of 1 to 140 characters of text")
    if line != line.strip():
        raise SystemExit("entry must not start or end with whitespace")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # Read back what was written and refuse to report success unless it
    # is byte for byte the line: the gate reads the file, not our memory.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != line:
            raise SystemExit("entry.txt does not match the line")
    print(line)


if __name__ == "__main__":
    main()
