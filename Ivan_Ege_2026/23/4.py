import sys
sys.setrecursionlimit(10000)

def f(x, y, s):
    if x > y + 6 or str(x)[-1] == '3' or 'AA' in s or 'AB' in s or 'BA' in s or 'BB' in s:
        return [0, s[-1]]
    elif x == y:
        return [1, s[-1]]
    else:
        return (f(x-1, y, s+'A')[0] + f(x-5, y, s+'B')[0] + f(x+7, y, s+'C')[0] + f(x*2, y, s+'D')[0], s[-1])

ss = ''
print(f(9, 60, '')[0])