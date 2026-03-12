import sys
sys.setrecursionlimit(10**6)
def f(x):
    if x>30:
        return f(x-6)+2048
    else:
        return 3*(g(x-5)+13)
def g(x):
    if x>=221337:
        return 2*x+50
    else:
        return g(x+11)-48
print(f(5078))