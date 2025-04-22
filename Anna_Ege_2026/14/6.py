import string
print(string.ascii_letters)
for x in ('0123456789ABCDEFG'):
    for y in ('0123456789ABCDEFG'):
        c1 = int(f'7{x}589{y}', 17)
        c2 = int(f'EE{x}{y}9AC', 17)
        if (c1 + c2) % 13 == 0:
            print(y, (int(f'7{x}5893', 17) + int(f'EE{x}39AC', 17)) // 13)