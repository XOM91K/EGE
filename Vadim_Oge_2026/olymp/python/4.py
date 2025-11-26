ALPHABET = "abcdefghijklmnopqrstuvwxyz1234567890"
def yoda_cipher(text: str) -> str:
    shift = -10
    text = text.lower()
    encrypted = ""
    for ch in text:
        if ch in ALPHABET:
            index = ALPHABET.index(ch)
            encrypted += ALPHABET[(index + shift) % len(ALPHABET)]
        else:
            encrypted += ch
    return encrypted

enc = 'wy3{wd9_4rc_pvdq_lc_7a4r_9j5}'
print(yoda_cipher(enc))