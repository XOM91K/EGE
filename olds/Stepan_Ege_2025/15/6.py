for A in range(1, 1000):
        can = True
        for x in range(1, 1000):
            if (((x % 13 == 0) <= (not(40 <= x <= 60))) or (A < x + 20)) == 0:
                can = False
                break
        if can:
            print(A)