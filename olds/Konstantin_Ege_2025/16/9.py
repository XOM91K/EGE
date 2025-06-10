import sys
sys.setrecursionlimit(30000)
def f(n):
    if n <= 2:
        return 5
    if n > 2:
        return f(n - 2) + n
print(f(23023))