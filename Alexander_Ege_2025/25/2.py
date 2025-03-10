import fnmatch
for x in range(27451, 10 ** 10, 27451):
    if fnmatch.fnmatch(str(x), '54?1?3*7'):
        print(x, x // 27451)