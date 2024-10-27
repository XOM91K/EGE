import sys
sys.setrecursionlimit(100000)
def F(n):
    if n < 5:
        return 4**4
    if n > 4:
        return 4 * F(n - 1) + 4
print(F(4048)/F(4036))