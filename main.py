"""Entry for make.fun's "One Word From Grandma" bounty.

Writes exactly one word to entry.txt in the output directory
(1-30 UTF-8 characters, per the sealed gate): the single word
a grandma would text about AI. The same bytes are written on
every run.
"""

import os

# Draft: "Robot" — accurate, but it is the obvious pick and it
# reads like a dictionary, not like a text from grandma.
# Revised: "Robit" — grandma's own spelling of the word, the
# way she would actually type it to a grandchild: warm, a
# little baffled, still unmistakably about the machine.
WORD = "Robit"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
