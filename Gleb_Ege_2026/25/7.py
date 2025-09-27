import fnmatch
for x in range(18579, 10 ** 10, 18579):
    if fnmatch.fnmatch(str(x), '54?1?3*7'):
        print(x, x // 18579)