import sys, functools
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(1000000)
@functools.lru_cache(100)

def f(n):
    if n ==1:
        return 1
    if n > 1:
        return f(n-1) * (n // 2) + 1
for n in range(1,10005):
    f(n)
print(sum(map(int, str(f(10000))[-18:])))