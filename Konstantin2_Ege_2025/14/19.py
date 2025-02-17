ct = []
for x in '123456789abcdefghijklmno':
    c1 = int(f'8af7{x}11', 25)
    c2 = int(f'{x}da87', 25)
    for y in range(1, 101):
        if (c1 + c2) % y == 0:
            ct.append(y)
print(len(set(ct)))