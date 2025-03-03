for n in range(1, 1000):
    r = bin(n)[2:]
    if sum(map(int, r)) % 4 == 0:
        r = r + '1111'
    elif sum(map(int, r)) % 3 == 0:
        r = '111' + r
    else:
        r = r + '11'
    r = int(r, 2)
    if r < 450:
        print(r)