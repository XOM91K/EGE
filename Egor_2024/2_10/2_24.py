for x in range(100, 1000):
    d = x
    d -= x % 10
    d //= 10
    d = int(str(x)[-1] + str(d))
    if d == 237:
        print(x)