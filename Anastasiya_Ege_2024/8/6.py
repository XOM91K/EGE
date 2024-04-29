def tr(x):
    r = ''
    while x > 0:
        r = str(x % 3) + r
        x //= 3
    return r
for n in range(1, 1000):
    r = tr(n)
    rr = 0
    if n % 2 == 0:
        r = '1' + r + '00'
    else:
        for i in range(len(r)):
            rr += int(r[i])
        r += str(tr(rr))
    if int(r, 3) > 168:
        print(n)