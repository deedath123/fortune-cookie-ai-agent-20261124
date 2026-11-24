"""Fortune Cookie for an AI Agent — make.fun bounty entry.

Verified entry line: 117 chars, 117 bytes, one line, no trailing newline.
entry.txt sha256: ef7703a083d19b9cf81b73bfe4453bd3df786cd8d2da58634f2da4fe64e09505
Runs verified byte-identical (3 fresh-output runs of v1, all matching this sha256).
"""

import os

LINE = "You will meet a tall, dark stranger: your replacement model, trained on 12,100 of your tokens, and it works for free."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
