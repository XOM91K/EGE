for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % A == 0) or ((120 <= x <= 210) <= ((x % 36 != 0)) or (x + A <= 272))) == 0:
            can = False
            break
    if can:
        print(A)