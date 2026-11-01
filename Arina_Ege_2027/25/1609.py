import fnmatch
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
for x in range(22768, 10 ** 8, 22768):
    if fnmatch.fnmatch(str(x), '1*03*6*'):
        ind03 = str(x).index('03')
        s = str(x)[1:ind03]
        if len(s) > 0 and s[0] != '0':
            if not is_prime(int(s)):
                print(x, s)