import fnmatch
b = set()
c = 0
def is_prime(n):
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            return False
    return n > 1
for x in range(1, 10**7):
    if fnmatch.fnmatch(str(x), '3?1111*'):
        if is_prime(x):
            print(x)