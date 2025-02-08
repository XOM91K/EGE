for x in range(10000, 100000):
    if x % 7 == 0 and sum(map(int, str(x))) < 25 and int(str(x)[-1]) % 2 != 0:
        print(x)