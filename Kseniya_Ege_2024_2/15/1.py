for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((x % 6 == 0) <= (x % 14 != 0)) or ((x + A >= 70) and (A % 20 == 0))) == 0:
            can = False
    if can:
        print(A)
