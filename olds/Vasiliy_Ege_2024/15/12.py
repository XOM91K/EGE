for A in range(1, 300):
    can = True
    for x in range(1, 300):
        for y in range(1, 300):
            if (not((x + 5 < A) <= (y > A)) or (x * y >= 76)) == 0:
                can = False
    if can:
        print(A)