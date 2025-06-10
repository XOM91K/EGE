import sys
sys.setrecursionlimit(100000)
def F(n, x):
    if n >= 3000:
        return n
    if n < 3000:
        return n + 2 * x + F(n + 2, x)
for x in range(0, 5000):
    if F(28, x) - F(34, x) == 324:
        print(x)