import fnmatch
for x in range(7424, 10 ** 8 + 1, 10000):
    if fnmatch.fnmatch(str(x), '*15*7424'):
        k = 0
        g = 0
        if x % 111 == 0:
            k += 1
            g = 111
        if x % 113 == 0:
            k += 1
            g = 113
        if x % 127 == 0:
            k += 1
            g = 127
        if k == 1:
            print(x, x // g)