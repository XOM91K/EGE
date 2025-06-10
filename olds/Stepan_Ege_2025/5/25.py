def v4(n):
    s = ''
    while n > 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]

for n in range(1, 100000):
    r = v4(n)
    if n % 4 == 0:
        r = '2' + r + '03'
    else:
        r = r + v4((n % 4) * 5)
    r = int(r, 4)
    if r <= 567:
        print(n)