for x in range(10000, 100000):
    if x % 7 == 0 and x % 10 % 2 != 0:
        if sum(map(int, str(x))) < 25:
            print(x)