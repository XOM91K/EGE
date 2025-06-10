import fnmatch
ct = 0
for x in range(1917, 10 ** 10, 1917):
    if fnmatch.fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)