import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJK':
    c1 = int(f'2496{x}2', 21)
    c2 = int(f'8{x}223', 21)
    c3 = int(f'2331768{x}3', 21)
    if (c1 + c2 + c3) % 20 == 0:
        print((c1 + c2 + c3) // 20)