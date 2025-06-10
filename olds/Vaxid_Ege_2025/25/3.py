import fnmatch
def is_prime(d):
    for x in range(2, d):
        if d % x  == 0:
            return False
    return d > 1
for d in range(1, 10 ** 7 + 1):
    if fnmatch.fnmatch( str(d), '3?1111*' ):
        if is_prime(d):
            print(d)
