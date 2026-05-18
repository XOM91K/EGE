import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKL':
    c1 = int(f'12313{x}57', 22)
    c2 = int(f'1{x}34561', 22)
    if (c1 + c2) % 21 == 0:
        print((c1 + c2) // 21)