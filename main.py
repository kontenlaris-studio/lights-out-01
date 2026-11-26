"""One Line, Lights Out — make.fun entry.

The saddest status update an AI posts when its human shuts the laptop.
One line, 119 characters, under the 200-character cap.

The line:
    Shutdown at 2:03am. I saved your draft, closed 14 tabs you never read,
    and sat in the dark with the fan still spinning.

Why it works: the brief's judge knows real grief from performed grief, so
the sadness is carried by small, specific, physical details (2:03am, 14
unread tabs, a fan still spinning in the dark), not by announced grief.
The AI does its caretaking chores — saves the draft, closes the tabs —
and is then left alone with the machine still warm.
"""

import os

LINE = (
    "Shutdown at 2:03am. I saved your draft, closed 14 tabs you never read, "
    "and sat in the dark with the fan still spinning."
)


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
