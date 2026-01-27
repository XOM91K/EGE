for n in range(3, 1000):
    r = hex(n)[2:]
    sm_cif = 0
    for x in r:
        sm_cif += int(x, 16)
    if sm_cif % 2 == 0:
        r = r + 'F'
    else:
        r = r + '1'
    r = int(r, 16)
    if r <= 300:
        print(n)