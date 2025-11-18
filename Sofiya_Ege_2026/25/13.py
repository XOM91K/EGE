def f7(n):
    s=''
    while n>0:
        s=str(n%7)+s
        n//=7
    return s
import fnmatch
for x in range(333, 10**9, 333):
    a=f7(x)
    if fnmatch.fnmatch(str(a), '?213*5664'):
        print(x, x//333)