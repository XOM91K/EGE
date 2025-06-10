ct = 0
for A in range(1, 10000):
    can = True
    for x in range(1, 10000):
        if ((x % 12 == 0) and (70 <= x <= 80) and (x % A != 0)) == 1:
            can = False
            break
    if can:
        ct += 1
print(ct)