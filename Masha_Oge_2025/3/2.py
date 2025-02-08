for x in range(10_000, 100_000):
    if (x % 7 == 0) and sum(map(int, str(x))) < 25 and (x % 10) % 2 != 0:
        print(x)
# d = 557
# print(sum(map(int, str(d))))