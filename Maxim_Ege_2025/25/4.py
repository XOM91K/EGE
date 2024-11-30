import fnmatch
def is_prime(d):
    for x in range(2, d):
        if d % x == 0:
            return False
    return d > 1
print(is_prime(0))
for x in range(0,10**9,2627):
    if fnmatch.fnmatch(str(x),'7*53?3*1'):
        if is_prime(sum(map(int,str(x)))) == True:
            print(x, x // 2627)