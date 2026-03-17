import re


def isPrime(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return x > 1


for x in range(22768, 10 ** 8, 22768):
    m = re.findall(r'\b1([1-9]\d*)03\d*6\d*\b', str(x))
    if len(m) > 0 and not isPrime(int(m[0])):
        print(x, m[0])
