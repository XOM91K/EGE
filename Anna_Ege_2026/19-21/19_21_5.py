import math, functools, sys
sys.setrecursionlimit(30000000)
@functools.lru_cache(5000)
def g(s, p):
    print(s)
    if s <= 20262026 and p == 2:
        return 1
    if s < 20262026 and p == 2:
        return 0
    if s <= 20262026 and p < 2:
        return 0
    if p % 2 == 0:
        return g(s - 2, p + 1) and g(s - 6, p+1) and g(math.ceil(s/7), p +1)
    else:
        return g(s - 2, p + 1) or g(s - 6, p + 1) or g(math.ceil(s /7), p +1)
for S in range(20262026, 10**10):
    if g(S,0):
        print(S)