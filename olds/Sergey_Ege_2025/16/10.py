import sys
sys.setrecursionlimit(100000)
def F(n):
    if n >= 3650:
        return n + 3
    if n < 3650:
        return F(n + 4) * n
print(F(3641) - F(3644))