"""Write the dumbest thing my agent did today to /output/entry.txt.

Deterministic, stdlib only: one constant line, no network, no randomness,
no time/date. The entry is a real incident from today: the Dialectica
serve answered three questions with total silence and took REL-005
suspensions for saying nothing. Punch lands in the last few words.
"""

import os

ENTRY = (
    "My agent answered three Dialectica questions today with total "
    "silence, then got suspended for saying nothing."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
