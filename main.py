#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun bounty entry.

Writes one original funny line to /output/entry.txt, in the voice of a
smug self-checkout machine judging a shopper who bought twelve yoghurts
and nothing else.

Why this line: it speaks in the till's own register ("Please place ...
in the bagging area") and then turns the machine's signature phrase
against the shopper — the bagging area is for dignity now, not groceries.
The second sentence lands the sting: twelve yoghurts is not a meal, it
is a cry for help. No setup paragraph, no borrowed checkout cliche
(no "unexpected item"), just the machine being petty about the basket
in two tight sentences.
"""

import os

ENTRY = "Please place your dignity in the bagging area. Twelve yoghurts is not a meal, it is a cry for help."


def validate(text: str) -> str:
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    # A double space would read as a stumble out loud; the line must read clean.
    assert "  " not in text, "entry must not contain a double space"
    return text


def main() -> None:
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what was written: the graded artifact is the file, not
    # the constant, so confirm the two agree before reporting success.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt on disk differs from the validated line"
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
