import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKLMNO':
    c1 = int(f'11353{x}12', 25)
    c2 = int(f'135{x}21', 25)
    if (c1 + c2) % 24 == 0:
        print((c1 + c2) // 24)