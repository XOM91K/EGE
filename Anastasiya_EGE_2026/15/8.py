for A in range(20000, 1, -1):
    can = True
    for x in range(1, 20000):
        if (not ((x % 263 == 0) <= (x % A == 0)) and (x % 71 == 0)) == 1:
            can = False
            break
    if can:
        print(A)