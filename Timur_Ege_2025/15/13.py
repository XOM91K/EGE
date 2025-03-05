for A in range(1,10000):
    can = True
    for x in range(1,10000):
        if (((x % 12 == 0) <= (x % 42 != 0)) or (x + A >= 4096)) == 0:
            can = False
            break
    if can:
        print(A)