import sys
sys.setrecursionlimit(1000000)
def F(n):
    if n <= 800:
        return 1
    if n > 800:
        return F(n - 2) * (n - 560)
print(F(3404) / F(3399))