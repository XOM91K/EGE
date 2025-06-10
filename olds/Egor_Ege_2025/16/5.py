import sys
sys.setrecursionlimit(100000)
def F(n):
    if n >= 2010:
        return n
    if n < 2010:
        return F(n + 3) + F(n + 2) + F(n + 1)
print((F(2000) - 2 * (F(2002) + F(2003))) / F(2004))