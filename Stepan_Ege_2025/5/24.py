def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]

for n in range(4, 1000):
    r = v3(n)
    if str(r)[-2:] == '10':
        r = '2' + r
    else:
        r = '1' + r
    r = int(r, 3)
    if r > 130:
        print(n)