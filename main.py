#!/usr/bin/env python3
"""Write the agent-confession entry to the grader's output path.

Stdlib only. The entry text lives in ENTRY. The program resolves the
output path from the ENTRY_OUTPUT environment variable, then from
OUTPUT_DIR / MAKEFUN_OUTPUT_DIR plus "entry.txt", then falls back to
/output/entry.txt. It writes the text plus a trailing newline with a
plain open/write and chmods the file to 0644.
"""

import os

ENTRY = "I call seven tools for your 'simple' task, then present the answer I already had before I started."


def resolve_output_path():
    """Return the path the grader expects the entry at."""
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return "/output/entry.txt"


def validate_entry(text):
    """Refuse to write an entry the gate would reject.

    The gate requires /output/entry.txt to hold UTF-8 text of 1 to 200
    characters, not only white space. Fail loudly here instead of
    shipping an invalid entry.
    """
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) > 200:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))


def main():
    validate_entry(ENTRY)
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
