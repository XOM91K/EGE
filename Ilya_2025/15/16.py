for A in range(-1000, 1000):
    can = True
    for x in range(1, 1000):
        if (((50 <= x <= 80) <= (x % 7 != 0)) or ((x + A) >= 90)) == 0:
            can = False
            break
    if can:
        print(A)
