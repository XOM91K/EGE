import fnmatch
for x in range(62961, 10 ** 9 + 1, 62961):
    if fnmatch.fnmatch(str(x), '*31*65?'):
        print(x, x // 273)