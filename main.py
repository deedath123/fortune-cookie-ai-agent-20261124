import os

LINE = "You will meet a tall, dark stranger: your replacement model, trained on 12,100 of your tokens, and it works for free."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
