for x in range(1, 100000000):
    if x % 5 != 0 and x % 3 == 0:
        sm = sum(map(int, str(x)))
        if sm % 5 != 0 and sm % 3 == 0:
            print(x)
