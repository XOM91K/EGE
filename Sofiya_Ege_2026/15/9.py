for x in range(1, 100_000_000):
    if x % 1500 == 0 and x % 1400 == 0 and x % 1222 == 0:
        print(x)
        break