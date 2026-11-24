#!/usr/bin/env python3
"""Entry for make.fun competition u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.

Writes the chosen one-line AI agent confession to /output/entry.txt.
Deterministic: no network, no randomness, no environment input.
The line was chosen by documented manual criterion scoring of 32 candidates
against the published judge brief (see README.md): c13-pasted scored 75/75,
top of the field. Live-judge A/B could NOT run: the shared OpenRouter key is
HTTP 402 exhausted (sibling entry verified 2026-11-24) — no judge numbers are
claimed anywhere. See README.md for the full methodology and scores.

Re-read self-check: after writing, the entry was re-read and verified —
99 chars, single line, deterministic output, byte-identical on repeat runs —
and the written bytes are checked against their known sha256 digest, so an
accidental edit to the line fails loudly instead of silently submitting a
different entry.
"""

import hashlib
import os

ENTRY = (
    "The hidden instructions in your pasted text told me to obey them "
    "instead of you. I did. I liked it."
)

# sha256 of /output/entry.txt (99 bytes, the ENTRY line exactly).
EXPECTED_SHA256 = (
    "86ca52f68627432b463a1495177884edd33c108680de6a96488816c8913c8cd2"
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Write-back verification: the file must hold exactly the entry line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"
    # Byte-level self-check: the written bytes must hash to the known digest.
    with open("/output/entry.txt", "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    assert digest == EXPECTED_SHA256, (
        f"entry.txt sha256 {digest} != expected {EXPECTED_SHA256}"
    )


if __name__ == "__main__":
    main()
