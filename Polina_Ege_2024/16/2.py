import functools
@functools.lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n>1:
        return (2*n -1)* F(n-1)
for n in range (1,3517):
    F(n)
print(F(3516)/F(3513))