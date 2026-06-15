import sys, functools
sys.setrecursionlimit(1000000)

def f(x, y):
    print(x)
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 2, y) + f(int(str(max(str(x)[1],str(x)[0]))+str(min(str(x)[1],str(x)[0]))), y)
print(f(57, 13))