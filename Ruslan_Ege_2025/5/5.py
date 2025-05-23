def f(n):
    s = ''
    while n > 0:
        s = str(n%4)+s
        n //=4
    return s
for n in range(1, 10000):
    r = f(n)
    if sum(map(int, r)) % 2 == 0:
        r = '13' + r[2:] + '0'
    else:
        r = '2' + r[:-2] +'13'
    r = int(r, 4)
    if r == 167:
        print(n)