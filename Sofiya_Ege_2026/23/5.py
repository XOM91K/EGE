import functools
@functools.lru_cache(None)
def f(x, y):
    if x>y: return 0
    if x==y: return 1
    if x<y: return f(x+1, y)+f(x*2, y)+f(x*3, y)
ct = 0
for x in range(2, 16, 2):
    ct += f(x, 15)
print(ct)