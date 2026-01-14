for n in range(3, 1000):
    r = hex(n)[2:]
    sm = 0  # 12332aa
    for x in '0123456789abcdef':
        sm += r.count(x) * int(x, 16)
    if sm % 2 == 0:
        r += 'F'
    else:
        r += '1'
    r = int(r, 16)
    if r <= 300:
        print(n, r)
