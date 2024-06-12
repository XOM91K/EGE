import sys
sys.setrecursionlimit(100000)
def f(n):
    if n <= 7:
        return 1
    if n > 7:
        return n + 2 + f(n - 1)
print(f(2024) - f(2020))