import sys
sys.setrecursionlimit(100000)
def f(n):
    if n >= 2031:
        return 1
    if n < 2031:
        return n + 31 + f(n + 31)
print(f(31) - f(23))