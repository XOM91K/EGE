import fnmatch
def pr(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return x > 1
for x in range(0,10**7):
    if fnmatch.fnmatch(str(x),'3?1111*'):
        if pr(x):
            print(x)