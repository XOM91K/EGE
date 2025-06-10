for n in range(3, 10000):
    r = hex(n)[2:]
    if sum(map(int, str(int(r, 16)))) % 2 == 0:
        r = r + 'f'
    else:
        r = r + '1'
    r = int(r, 16)
    if r <= 300:
        print(n)