import fnmatch
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
for x in range(10 ** 7):
    if fnmatch.fnmatch(str(x), '3?1111*'):
        if is_prime(x):
            print(x)