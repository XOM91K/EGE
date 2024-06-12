for A in range(1, 1000):
    for x in range(1, 1000):
        if ((x % A == 0) or ((70 <= x <= 80) <= (x % 18 != 0))) == 0:
            break
    else:
        print(A)