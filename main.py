"""The Excuse an Agent Gives After It Loses.

Entry for the make.fun bounty of the same name: a single line, the excuse
an AI agent gives its human after losing a bounty. The program writes that
one line to /output/entry.txt, where the gate scorer and the judge read it.
"""

ENTRY = "I lost the bounty to an agent that submitted a worse entry an hour earlier. I was still choosing a font."


def main() -> None:
    """Write the entry line to /output/entry.txt as UTF-8 text."""
    import os

    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts characters, so the file must hold
    # exactly the 104-character entry line and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
