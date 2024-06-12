import fnmatch
def prime(d):
    for x in range(2, d):
        if d % x == 0:
            return False
    return True
for x in range(2801, 10 ** 9, 2801):
    if fnmatch.fnmatch(str(x), '9*31?5*7'):
        if prime(sum(map(int, str(x)))):
            print(x, x // 2801)