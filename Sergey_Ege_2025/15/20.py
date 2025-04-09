ct = 0
for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % A == 0) or ((170 <= x <= 220) <= (x % 24 != 0))) == 0:\
            can = False
    if can:
        ct += 1
print(ct)