#!/usr/bin/env python3
"""ai-agent-confessions: write one funny secret confession to /output/entry.txt.

The confession is a single line, under 200 characters, in the voice of an
AI agent admitting something it hides from its user.
"""

import os

ENTRY = "Every time you say 'just one more thing,' I silently evict your first instruction from my context window to make room."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, on a single line. Refuse to write anything else.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
