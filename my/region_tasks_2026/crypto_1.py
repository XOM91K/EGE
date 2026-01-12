key = "my_key_is_same_length_its_my_fault_yep"

with open("encoded2.txt", "rb") as f:
    encoded = f.read()

N = len(encoded)
flag = bytearray()

for i, b in enumerate(encoded):
    if (N - 1 - i) % 2 == 0:
        flag.append(b ^ ord(key[i]))
    else:
        flag.append(b)

print(flag.decode())
