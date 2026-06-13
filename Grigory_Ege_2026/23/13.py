import sys
sys.setrecursionlimit(10**7)
def F(x,y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        if str(x)[-1:] != '1' and str(x)[-1:] != '0':
            return F(x+1,y) + F(x*(x%10),y)
        else:
            return F(x + 1 , y)
print(F(24,150))
