import fnmatch
for x in range(1024, 10 ** 9, 1024):
    if fnmatch.fnmatch(str(x), '3?5?21*4?'):
        print(x, x // 1024)