import functools
@functools.lru_cache(None)
def F(n):
    if n<65000:
        return F(9+n)+13020
    if n>=65000:
        return 4*(G(n-4)-12)
@functools.lru_cache(None)
def G(n):
    if n>=111700:
        return G(n-17)+344
    if n<111700:
        return 8*n-4
for n in range(0,160000):
    G(n)
for n in range(160000,0,-1):
    F(n)
print(F(4975))