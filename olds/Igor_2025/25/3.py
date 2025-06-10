import fnmatch
def get_max_del(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return n // x
    return 0
for x in range(1, 3162 + 1):
    x **= 2
    if fnmatch.fnmatch(str(x), '3*52?'):
        print(x, get_max_del(x))
