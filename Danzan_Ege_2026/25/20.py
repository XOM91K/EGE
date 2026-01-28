import fnmatch, re
def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False
    return d > 1

for x in range(22768, 10 ** 8, 22768):
    s = str(x)
    if fnmatch.fnmatch(s, '1*03*6*'):
        r = re.findall(r'1(\d+)03\d*6\d*', s)
        if len(r) > 0:
            r = r[0]
            if is_prime(int(r)) == False:
                print(x, r)