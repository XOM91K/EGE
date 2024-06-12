import fnmatch
def get_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
for x in range(1, 10**7):
    if fnmatch.fnmatch(str(x), '3?1111*'):
        if get_prime(x):
            print(x)