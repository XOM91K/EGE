for n in range(3, 1000):
    r = hex(n)[2:]
    if sum(map(int, str(int(r, 16)))) % 2 == 0:
        r += 'f'
    else:
        r += '1'
    if int(r, 16) <= 300:
        print(int(r, 16), n)