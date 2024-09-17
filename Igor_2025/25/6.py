def m(d):
    M = 0
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            M = x + (d // x)
            break
    return M
ct = 0
for x in range(800_001, 10_000_000):
    if str(m(x))[-1] == '4':
        print(x, m(x))
        ct += 1
    if ct == 5:
        break