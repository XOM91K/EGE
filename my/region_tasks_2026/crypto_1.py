key = "key_with_the_same_length_maybe_little_bit_more_hue_hue_hue"

with open("encoded.txt", "rb") as f:
    encoded = f.read()

N = len(encoded)
flag = bytearray()

for i, b in enumerate(encoded):
    if (N - 1 - i) % 2 == 0:
        flag.append(b ^ ord(key[i]))
    else:
        flag.append(b)

print(flag.decode())
