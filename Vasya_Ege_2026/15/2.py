for x in range(1, 100_000_0000):
    if x % 640 == 0 and x % 370 == 0 and x % 680 == 0:
        print(x)