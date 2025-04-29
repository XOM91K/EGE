import string
for x in '0123456789AB':
    c1 = int(f'154{x}3', 12)
    c2 = int(f'1{x}365', 12)
    if (c1 + c2) % 13 == 0:
        print((c1 + c2) // 13)