s = 'cdc7ffc7f1d7e543c99fc541c949c94341fd9f43c79fedcbfd9f47e343414d4b534ddb00'
s = bytes.fromhex(s)
a = []
for x in s:
    c1 = (x >> 7 & 0xFF) | (x << 1 & 0xFF)
    c2 = c1 ^ 0x42
    c3 = (c2 << 6 & 0xFF) | (c2 >> 2 & 0xFF)
    a.append(c3)
print(bytes(a))



