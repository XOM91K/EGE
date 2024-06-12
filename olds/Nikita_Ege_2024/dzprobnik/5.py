def th(x):
    t = ""
    while x > 0:
        t += str(x % 6)
        x = x // 6
    return t[::-1]


for n in range(1, 10000):
    r = th(n)
    if n % 3 == 0:
        r += r[:2]
    else:
        r += th(n % 3 * 10)
    r = int(r, 6)
    print(r)
