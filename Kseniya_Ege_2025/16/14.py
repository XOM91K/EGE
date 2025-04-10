#import functools
#@functools.lru_cache(None)
#import sys
#sys.setrecursionlimit(5000)
import sys, functools
sys.setrecursionlimit(5000)
@functools.lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * F(n -1)
for n in range(1, 4000):
    F(n)
print((F(2024)+2 *F(2023))/F(2022))