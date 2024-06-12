import sys
sys.setrecursionlimit(10000)
def f(n):
    if n >= 2020:
        return n
    if n < 2020:
        return n + 2 + f(n + 3)
print(f(2012) - f(2023))