n = 160100
for A in range(n, 1, -1):
    can = True
    for x in range(1, n):
        if ((x % 256 == 0) <= ((x % A != 0) <= (x % 625 != 0))) == 0:
            can = False
            break
    if can:
        print(A)
        break