import string
print(string.ascii_uppercase)
for x in '0123456789abcdefghi':
    c1 = int(f'a3{x}74', 19)
    c2 = int(f'{x}40846', 19)
    if (c1 + c2) % 9 == 0:
        print((c1 + c2) // 9)