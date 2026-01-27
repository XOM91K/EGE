import functools
@functools.lru_cache(None)
def F(n):
    if n<31054:
        return F(n+4)+3020
    if n>=31054:
        return 3*(G(n-2)-15)
@functools.lru_cache(None)
def G(n):
    if n>=28:
        return G(n-5)-15
    if n<28:
        return 3*n-4
for n in range(-100,1000000):
    G(n)
for n in range(1000000, -100, -1):
    F(n)
print(F(15))