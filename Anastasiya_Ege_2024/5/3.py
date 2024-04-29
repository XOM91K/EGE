def v3(n):
    ost = ''
    while n > 0:
        ost = str(n % 3) + ost
        n //= 3
    return ost
for n in range(1,1000):
    r = v3(n)
    if n % 4 == 0:
        r += r[-3:]
    else:
        r += v3(n % 4 * 4)
    r = int(r, 3)
    if r < 127:
        print(r)