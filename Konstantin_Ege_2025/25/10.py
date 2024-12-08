import fnmatch
def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
for x in range(333, 10**9, 333):
    chislo_7 = v7(x)
    if fnmatch.fnmatch(chislo_7, "?213*5664"):
        print(x, x // 333)