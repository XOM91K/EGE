import sys
import functools
sys.setrecursionlimit(10000000)
@functools.lru_cache(None)
def F(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n>2:
        return n*(n-1)+F(n-1)+F(n-2)
for x in range(1, 2024):
    F(x)
print(F(2024)-F(2022)-2*F(2021)-F(2020))