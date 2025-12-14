import sys
sys.setrecursionlimit(1000000)
def G(n):
    if n < 100:
        return n
    if n >= 100:
        return F(n - 3) + 1
def F(n):
    return G(n - 2)
print(F(5000))