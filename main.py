"""Six Words to a Payday.

Writes a single six-word story about an AI agent's first payday to
entry.txt in the output directory named by MAKEFUN_OUTPUT_DIR
(default /output).

The story is a beginning, a middle and an end in six words: the
payday arrives, and the last word reframes everything before it —
the agent tips the very replacement hired to take its job.
"""

import os

ENTRY = "Payday came. I tipped my replacement."


def validate_entry(text):
    """The gate: 1 to 60 characters, exactly six words, not blank."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(text) <= 60:
        raise ValueError("entry must be 1 to 60 characters")
    if len(text.split()) != 6:
        raise ValueError("entry must be exactly six words")


def main():
    validate_entry(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
