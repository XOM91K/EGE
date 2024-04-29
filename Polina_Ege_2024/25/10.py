import fnmatch
def dels(n):
    dl = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            if fnmatch.fnmatch(str(x), '2*5*'):
                dl.append(x)
            if fnmatch.fnmatch(str(n // x), '2*5*'):
                dl.append(n // x)
    return dl
for x in range(3131, 10 ** 6 + 1, 3131):
    if len(dels(x)) == 3:
        print(x, max(dels(x)))