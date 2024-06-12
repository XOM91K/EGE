import fnmatch
def dels(n):
    dl = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            if x % 2 == 0:
                dl.append(x)
            if (n // x) % 2 == 0:
                dl.append(n // x)
    return dl
ct = 0
for x in range(65001, 10 ** 10):
    d = dels(x)
    if len(d) >= 4 and fnmatch.fnmatch(str(x), '6*97*5?'):
        ct += 1
        print(x, sum(d))
    if ct == 7:
        break