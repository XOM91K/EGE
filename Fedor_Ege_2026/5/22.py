def v3(g):
    s = ''
    while g > 0:
        s += str(g %3)
        g //= 3
    return s[::-1]


for n in range(1,10000):
    r = v3(n)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        su = sum(map(int, r))
        de = v3(su)
        r += de
    r = int(r, 3)
    if r > 220:
        print(r)