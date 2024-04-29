for A in range(1, 10000):
    can = True
    for x in range(1, 10000):
        if ((x % 72 != 0) or (x % 495 == 0) or (x % A != 0)) == 0:
            can = False
            break
    if can:
        print(A)
        break