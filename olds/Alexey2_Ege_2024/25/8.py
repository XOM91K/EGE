def get_dels(n):
    dl = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if x != 7 and x % 10 == 7:
                dl.append(x)
            if (n // x) != 7 and (n // x) % 10 == 7:
                dl.append(n // x)
    return dl
ct = 0
for x in range(600_001, 600_001 * 5):
    if len(get_dels(x)) > 0:
        print(x, min(get_dels(x)))
        ct += 1
    if ct == 5:
        break