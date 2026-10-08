import sys
sys.setrecursionlimit(20000)
def F(n):
    if n < 65000:
        return F(9 + n) + 13020
    if n >= 65000:
        return 4 * (G(n - 4) - 12)
def G(n):
    if n >= 111700:
        return G(n - 17) + 344
    if n < 111700:
        return 8 * n - 4

print(2 * sum(map(int, str(F(4975)))))

# почему здесь не нужен functools ?