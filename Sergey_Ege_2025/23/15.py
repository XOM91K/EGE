import sys

sys.setrecursionlimit(100000000)
def F(x,y):
  if x < y:
    return 0
  if x == y:
    return 1
  if x > y:
    a = int(str(x**2)[0])
    b = sum(map(int,str(x)))
    return F(x - a,y) +F(x-b,y)
print(F(32,1))
#Killed ?