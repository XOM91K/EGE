for A in range(1, 5000):
    can = True
    for x in range(1, 5000):
        if (((x & 673 != 0) or (x & 189 != 0)) <= (x & A > 0)) == 0:
            can = False
            break
    if can:
        print(A)