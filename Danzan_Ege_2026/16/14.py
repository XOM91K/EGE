import sys
sys.setrecursionlimit(10000000)
def F(n):
    if n > 30:
        return F(n - 6) + 2048
    if n <= 30:
        return 3*(G(n - 5) + 13)
def G(n):
    if n >=221337:
        return 2*n+50
    if n < 221337:
        return G(n + 11) - 48
print(F(5078))