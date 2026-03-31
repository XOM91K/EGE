n = 18800
for A in range(n, 1, -1):
    can = True
    for x in range(1, n):
        if ((not((x % 263 == 0) <= (x % A == 0))) and (x % 71 == 0)) == 1:
            can = False
            break
    if can:
        print(A)
        break