import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKL':
    c1 = int(f'98{x}79641', 22)
    c2 = int(f'25{x}49', 22)
    c3 = int(f'63{x}5', 22)
    if (c1 + c2 + c3) % 21 == 0:
        print((c1 + c2 + c3) // 21)