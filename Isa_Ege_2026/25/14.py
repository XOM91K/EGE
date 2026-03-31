import fnmatch

def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
for x in range(22768, 10 ** 8, 22768):
    if fnmatch.fnmatch(str(x), '1*03*6*'):
        st = str(x)[1:str(x).index('03')]
        if st != '' and st[0] != '0':
            if is_prime(int(st)) == False:
                print(x, st)
# d = '59444489'
# print(d[2:6])

# 12203648 22
# 14503216 45
# 15960368 596
# 18032256 8