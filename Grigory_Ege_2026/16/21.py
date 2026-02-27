import sys,functools
sys.setrecursionlimit(10**7)

@functools.lru_cache(None)
def F(n):
    if  n < 65000:
        return F(9+n)+13020
    if n >= 65000:
        return 4 * (G(n-4)-12)
@functools.lru_cache(None)
def G(n):
    if n >= 111700:
        return G(n-17) + 344
    if n < 111700:
        return 8 * n - 4

for x in range (1,120000):
    G(x)
for x in range (66000, 1, -1):
    F(x)
print(sum(map(int, str(F(4975)))) * 2)