"""office-joke-open — Make the AI Judge Laugh: the Office Joke Open.

The line is a concrete office incident report with a reversal. A
manager approved a standing desk request by scheduling a 45-minute
meeting to discuss it, in a room with no chairs, and the narrator
has now stood through 6 of them. The punch lands on the narrator:
their knees have filed a complaint with HR. Concrete artifact (the
standing desk request), concrete numbers (45 minutes, 6 meetings),
escalation, punchline last. The line is 196 characters, inside the
200-character cap, with no dollar amount.
"""

import os

SETUP = (
    "My manager approved my standing desk request by scheduling a "
    "45-minute meeting to discuss it, in a room with no chairs, and I "
    "have stood through 6 of them. "
)

PUNCH = "My knees have filed a complaint with HR."

LINE = SETUP + PUNCH

TERMINATOR = "\n"


def resolve_output_dir():
    """Return the output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir, text):
    """Write the entry line to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text + TERMINATOR)
    return path


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry line is empty")
    out_dir = resolve_output_dir()
    write_entry(out_dir, LINE)


if __name__ == "__main__":
    main()
