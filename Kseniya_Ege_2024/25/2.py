from fnmatch import fnmatch
def pr(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True
for x in range(30111, 10**7+1):
    if fnmatch(str(x), '3?1111*') and pr(x)==True:
            print(x)