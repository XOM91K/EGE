import sys
sys.setrecursionlimit(1_000_000)
def f(n):
    if n<19: return 5
    if n>=19: return (n+4)*f(n-7)
print((f(157163)//234 + f(157149)//533) // f(157142))