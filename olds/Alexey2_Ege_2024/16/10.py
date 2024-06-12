import sys
sys.setrecursionlimit(10000)
def F(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return n//2 * F(n-1)
    else:
        return (n-1)//2 *F(n-1)
print((F(2024) - F(2022))//F(2021))