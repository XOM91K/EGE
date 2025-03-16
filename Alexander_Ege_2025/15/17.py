for E in range(0, 1000000):
    can = True
    for x in range(0, 1000000):
        if ((15 <= x <= 40) <= ((not(21 <= x <= 63) and not(7 <= x <= E)) <= (not(15 <= x <= 40)))) == 0:
            can = False
            break
    if can:
        print(E)
        break