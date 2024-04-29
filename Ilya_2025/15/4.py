for A in range(1, 100000):
    can = True
    for x in range(1, 100000):
        if ((x + A >= 160) or ((x % 7 == 0) <= (x - 17 <= 0))) == 0:
            can = False
            break
    if can:
        print(A)
        break