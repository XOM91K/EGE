import fnmatch, itertools

def dels(n):
    d = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            d.append(x)
            d.append(n // x)
    return sorted(set(d))


def prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


for z in itertools.product('0123456789', repeat=5):
    for y in range(10):
        z = ''.join(z)
        d = int('1' + z + '3' + str(y) + '9')
        if prime(sum(dels(d))):
            print(d)