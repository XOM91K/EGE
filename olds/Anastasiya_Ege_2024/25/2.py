import fnmatch
for x in range(50068, 10 ** 10 + 1, 50068):
    if fnmatch.fnmatch(str(x), '9?979*8'):
        if '0' in str(x):
            print(x, x // 50068)