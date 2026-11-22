#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a quiet library mystery,
written to intrigue the AI judge reading it. Deterministic: every run
writes the exact same bytes.
"""

import os
import shutil

TEXT = (
    "Every Friday for a year, the same library book has come back on time, "
    "a different flower pressed between the same two pages. "
    "Today the flower is one the librarian has never seen before "
    "\u2014 and it is still warm from the sun."
)


def main() -> None:
    # The gate allows 1 to 280 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry text out of gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Empty the output directory's contents without deleting the
    # directory itself: the grader mounts /output as a volume, and
    # removing it would fail.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    data = TEXT.encode("utf-8")
    print(f"wrote {entry_path}: {len(TEXT)} chars, {len(data)} bytes")


if __name__ == "__main__":
    main()
