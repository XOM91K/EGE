import fnmatch
def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
for x in range(333, 10 ** 9, 333):
    if fnmatch.fnmatch(v7(x), '?213*5664'):
            print(x, x // 333)