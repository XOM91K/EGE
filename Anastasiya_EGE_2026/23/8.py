import sys, functools
sys.setrecursionlimit(10000000)
@functools.lru_cache(None)
def f(st, fn, s):
    if st > fn or s.count('B') > 3:
        return 0
    if st == fn:
        return 1
    if st<fn:
        return f(st + 3, fn, s + 'A') + f(st + 4, fn, s + 'B') + f(st ** 2, fn, s + 'C')

# for x in range(16777217):
#     f(4, x, '')
print(f(4, 61, ''))