import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFG':
    c1 = int(f'819{x}6{x}32', 17)
    c2 = int(f'45656925{x}', 17)
    c3 = int(f'771377{x}1', 17)
    if (c1 + c2 + c3) % 16 == 0:
        print((c1 + c2 + c3) // 16)
