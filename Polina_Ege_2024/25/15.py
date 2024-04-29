import fnmatch
def prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
def dels(n):
    dl = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if prime(x):
                dl.append(x)
            if prime(n // x):
                dl.append(n // x)
    return list(set(dl))
import itertools
for x in range(10 ** 4 + 1):
    if fnmatch.fnmatch(str(x), '*2?2'):
        g = dels(x)
        can = False
        mx = 0
        for y in itertools.product(g, repeat=7):
            if y[0] * y[1] * y[2] * y[3] * y[4] * y[5] * y[6] == x:
                mx = max(y)
                can = True
                break
        if can:
            print(x, mx)