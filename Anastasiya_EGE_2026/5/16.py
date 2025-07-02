for n in range(1, 1000):
    r = bin(n)[2:]
    sm = sum([int(x) for x in str(n)])
    if sm % 2 == 0:
        r += '0'
    else:
        r += '1'
    n = int(r, 2)
    if sum([int(x) for x in str(n)]) % 2 == 0:
        r += '0'
    else:
        r += '1'
    n = int(r, 2)
    if sum([int(x) for x in str(n)]) % 2 == 0:
        r += '0'
    else:
        r += '1'
    r = int(r, 2)
    if r > 2064:
        print(r)
