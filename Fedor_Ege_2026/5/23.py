for n in range(1, 5000):
    r = bin(n)[2:]
    if n % 5 == 0:
        r += '11'
    else:
        f = n // 5
        f = bin(f)[2:]
        r += f
    r = int(r, 2)

    if r >= 783:
        print(n)