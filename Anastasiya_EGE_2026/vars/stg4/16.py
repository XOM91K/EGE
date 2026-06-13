import sys, functools
sys.setrecursionlimit(100000)
def F(n):
    if n > 29999:
        return n + F(n - 5)
    else:
        return n + G(n - 2)
def G(n):
    if n < 30000:
        return 10 + n + G(n + 3)
    else:
        return n ** 2
print(F(75_000))