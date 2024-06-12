import fnmatch
def get_chet_dels(n):
    l = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            if x % 2 == 0:
                l.append(x)
            if (n // x) % 2 == 0:
                l.append(n // x)
    return sorted(set(l))
k = 0
for x in range(65001, 65001 * 100):
    d = get_chet_dels(x)
    if len(d) >= 4 and fnmatch.fnmatch(str(x), '6*97*5?'):
        print(x, sum(d))
        k += 1
    if k == 7:
        break