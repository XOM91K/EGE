ct = 0
for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % A == 0) or ((x in range(170, 221)) <= (x % 24 != 0))) == 0:
            can = False
            break
    if can:
        print(A)
        ct += 1
print(ct)