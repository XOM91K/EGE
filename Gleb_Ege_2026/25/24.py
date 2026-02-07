import fnmatch
def f(n):
    l = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
    return sorted(set(l))
ct = 0
for x in range(31622, 100000):
    x = x ** 2
    a = f(x)
    if len(a) == 45:
        if fnmatch.fnmatch(str(x), '1*2*7*04'):
            print(x, a[-2])
            ct += 1
            if ct == 5:
                break