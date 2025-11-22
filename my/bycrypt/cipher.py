import base64

def main() -> None:
    with open("encrypted.txt", "r", encoding="ascii") as f:
        flag_text = f.read()
    data = flag_text.encode("ascii")
    for _ in range(10):
        data = base64.b64decode(data)
    encrypted = data.decode("ascii")
    print(encrypted)
    with open("flag.txt", "w", encoding="ascii") as f:
        f.write(encrypted)


if __name__ == "__main__":
    main()