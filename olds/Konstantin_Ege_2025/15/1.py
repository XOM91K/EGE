for A in range(1, 1000):
    for x in range(1, 1000):
        if not(((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 100)):
            break
    else:
        print(A)