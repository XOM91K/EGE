for A in range(1, 1000):
    for x in range(1, 1000):
        if (((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 100)) == 0:
            break
    else:
        print(A)