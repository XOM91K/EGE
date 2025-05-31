import functools,sys
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def g(x,y,s):
    if x == y and s[-3:] == 'ACC':
        return 1
    if x > y or s.count('B') > 3:
        return 0
    if x < y:
        return g(x+3,y,s+'A')+g(x+4,y,s+'B')+g(x**2,y,s+'C')
for x in range(1, 16777216):
    g(1, x, '')
print(g(4,16777216,''))