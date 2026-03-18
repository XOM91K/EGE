n = 36000
for A in range(n, 1, -1):
    can = True
    for x in range(1, n + 1):
        if ((x % 465 == 0) <= ((x % A != 0) <= (x % 385 != 0))) == 0:
            can = False
            break
    if can:
        print(A)
        break