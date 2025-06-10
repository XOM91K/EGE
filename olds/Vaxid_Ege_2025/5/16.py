d = []
for n in range(3, 1000):
    r = hex(n)[2:]
    if sum(map(int, str(int(r, 16)))) % 2 == 0:
        r += 'F'
    else:
        r += '1'
    r = int(r, 16)
    if r <= 300:
        d.append(n)
print(max(d))