for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 5 == 0:
        r = r[0:3] + r
    else:
        r += bin((n % 5) * 5)[2:]
    r = int(r, 2)
    if r < 313:
        print(n)
