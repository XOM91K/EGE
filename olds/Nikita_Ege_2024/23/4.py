import sys, functools
sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def F(x, y, a, c, s):
    if x > y:
        return 0
    if x == y and (s == '1323123'):
        return 1
    if x == y and (s != '1323123'):
        return 0
    if x < y:
        return F(x + 3, y, a, c, s + '1') + F(x * a, y, a, c, s + '2') + F(x + c, y, a, c, s + '3')
for a in range(1, 100):
    for b in range(1, 100):
        if F(5, 329, a, b, '') > 0:
            print(a, b)
