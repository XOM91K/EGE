import sys,functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if  n > 2024:
        return 2
    if n == 2024:
        return  1
    if n < 2024 :
        return n * (n+1)+F(n+1)- F(n+2)
for n in range(2021,1, -1):
    F(n)
print(F(100)-F(10)+F(2020))