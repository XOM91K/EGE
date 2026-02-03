import re
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
for x in range(22768, 10 ** 8, 22768):
    m = re.findall(r'1\d+03\d*6\d*', str(x))
    if len(m) > 0 and m[0] == str(x):
        m2 = re.findall(r'1(\d+)03\d*6\d*', str(x))
        if is_prime(int(m2[0])) == False:
            print(x, m2[0])