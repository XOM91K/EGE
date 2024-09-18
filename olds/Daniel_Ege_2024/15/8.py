ct = 0
for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((A % 25 == 0) and (((x % 24 == 0) and (x % 75 == 0)) <= (x % A == 0))) == 0:
            can = False
    if can:
        ct += 1
print(ct)