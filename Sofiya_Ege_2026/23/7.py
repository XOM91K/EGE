import sys
sys.setrecursionlimit(1000_000)
def f(x, y, k, flag):
    if x == 5:
        flag = True
    if x > 5 and flag == False:
        return 0
    if x>y or '11' in k or '22' in k or '33' in k or x==6: return 0
    if x==y: return 1
    if x<y: return f(x+1, y, k+'1', flag)+f(x+3, y, k+'2', flag)+f(x**2, y, k+'3', flag)
print(f(1, 25, '', False))