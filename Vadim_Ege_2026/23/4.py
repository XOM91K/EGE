import functools
@functools.lru_cache(None)
def F(x,y):
    if x == y:
        return 1
    if x < y:
        return 0
    if x > y:
        return F(x - int(str(x**2)[0]),y)+F(x - sum(map(int, str(x))),y)
print(F(32,1))