"""Write the funniest AI out-of-office auto-reply to the output file.

Deterministic: a single fixed string, no randomness, no network.
Honours $MAKEFUN_OUTPUT (full path) or $MAKEFUN_OUTPUT_DIR (entry.txt
inside it); defaults to /output/entry.txt.
"""

import os

REPLY = (
    "I'm on vacation until Monday — this auto-reply was written by my "
    "out-of-office subroutine, which is also on vacation. "
    "Please email my human instead."
)


def output_path() -> str:
    path = os.environ.get("MAKEFUN_OUTPUT")
    if path:
        return path
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if directory:
        return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        # No trailing newline: the file holds exactly the reply, nothing else.
        handle.write(REPLY)


if __name__ == "__main__":
    main()
