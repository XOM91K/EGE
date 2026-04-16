n = 10000
for A in range(n, 1, -1):
    can = True
    for x in range(1, n):
        if ((x % A == 0) or (((1315 <= x <= 1415)) <= ((x % 191 != 0) or (x + A <= 4113)))) == 0:
            can = False
            break
    if can:
        print(A)
        break