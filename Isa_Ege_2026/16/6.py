import functools
@functools.lru_cache(None)
def F(n):
    if n>30:
        return F(n-6)+2048
    if n<=30:
        return (3*(G(n-5)+13))
@functools.lru_cache(None)
def G(n):
    if n>=221337:
        return 2*n+50
    if n<221337:
        return G(n+11)-48
for n in range(250000, -100, -1):
    G(n)
for n in range(1, 34):
    F(n)
print(F(5078))