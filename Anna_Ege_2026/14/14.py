import string
print(string.ascii_letters)
ct = 0
t = set()
tt = list()
for x in '123456789ABCDEFGHIJKLMNO':
    c1 = int(f'8AF7{x}11', 25)
    c2 = int(f'{x}DA87', 25)
    for y in range(1, 101):
        if ((c1 + c2) % y) == 0:
            t.add(y)
            tt.append(y)
print(len(t))
print(len(tt))