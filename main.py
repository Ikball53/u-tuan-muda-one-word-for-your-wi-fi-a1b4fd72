#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry writer (stdlib only, deterministic).

Writes a single word to /output/entry.txt as exact UTF-8 bytes with no
trailing newline. The word is "Ghosting": home Wi-Fi that is right there,
full bars, and then — mid-call, mid-download, mid-sentence — simply gone,
no explanation, no goodbye. It is the most lived-in Wi-Fi experience
there is, and the funniest one-word way to say it.
"""

import os

ENTRY_WORD = "Ghosting"


def main() -> int:
    output_path = "/output/entry.txt"
    # Gate guard: one word, 1-20 characters, no whitespace at all.
    assert ENTRY_WORD.isalpha() and 1 <= len(ENTRY_WORD) <= 20
    assert " " not in ENTRY_WORD and "\n" not in ENTRY_WORD
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Exact bytes, no trailing newline, UTF-8.
    with open(output_path, "wb") as handle:
        handle.write(ENTRY_WORD.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
