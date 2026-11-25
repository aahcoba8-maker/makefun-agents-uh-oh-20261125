"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The word is "buffering": the universal sound of a machine stalling mid-task.
It is a genuine machine-voice reaction to being lost, funny on its own with no
caption, instantly readable, and fresh next to the obvious "oops" / "uh-oh".
"""

import os

WORD = "buffering"


def main():
    # Self-gate mirroring the sealed scorer: UTF-8, 1-99 chars, one word,
    # not whitespace-only.
    assert 1 <= len(WORD) <= 99, "word must be 1-99 characters"
    assert WORD.strip(), "word must not be blank"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"{WORD} ({len(WORD)} chars)")


if __name__ == "__main__":
    main()
