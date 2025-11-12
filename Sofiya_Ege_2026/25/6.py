import fnmatch
def is_prime(d):
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            return False
    return d>1
for x in range(2627, 10**9, 2627):
    if fnmatch.fnmatch(str(x), '7*53?3*1'):
        if is_prime(sum(map(int, str(x)))):
            print(x, x//2627)