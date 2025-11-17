import sys,functools
sys.setrecursionlimit(10**6)
@functools.lru_cache(None)
def F(x,y, s):
    if x > y or 'ab' in s:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + 3,y, s+'a')+F(x *5,y, s+'b') + F(x*7,y,s+'c')
print(F(1,1000, ''))