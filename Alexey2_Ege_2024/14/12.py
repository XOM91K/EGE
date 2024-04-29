import collections
def sev(d):
    s = []
    while d > 0:
        s.append(d % 17)
        d //= 17
    return s[::-1]
n = 5 * 3  ** 1917 + 6 * 2 ** 1878 + 7 * 3 ** 1870 - 1991
r = sev(n)
print(collections.Counter(r))