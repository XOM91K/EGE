from functools import lru_cache
import sys
sys.setrecursionlimit(100000)
@lru_cache(None)
def f(a, b, c):
    print(a, b, c)
    if a==b and c==68:
        return 1
    if a>=b:
        return 0
    if a<b:
        return f(a+3, b, c+1) + f(a-2, b, c+1)

k=0
for b in range(-30, 30):
    if f(1, b, 0)==1:
        print('?')
        k+=1
print(k)