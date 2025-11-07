import fnmatch
def m(n):
    l = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            l.append(d)
            l.append(n // d)
    return len(l)
ct = 0
for x in range(2627, 10 ** 9, 2627):
    if fnmatch.fnmatch(str(x), '7*53?3*1'):
        if m(sum(map(int, str(x)))) == 2:
            print(x, x // 2627)