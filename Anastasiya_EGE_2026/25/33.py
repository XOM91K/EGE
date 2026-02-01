import re
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
for x in range(22768,10**8,22768):
    m = re.findall(r'1[^0]\d*03\d*6\d*', str(x))
    sostavnoe = re.findall(r'1([^0]\d*)03\d*6\d*', str(x))
    if len(m) > 0 and int(m[0]) == x and is_prime(int(sostavnoe[0])) == False:
       print(x, sostavnoe[0])