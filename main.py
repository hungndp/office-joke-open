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

LINE = (
    "My manager approved my standing desk request by scheduling a "
    "45-minute meeting to discuss it, in a room with no chairs, and I "
    "have stood through 6 of them. My knees have filed a complaint with HR."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
