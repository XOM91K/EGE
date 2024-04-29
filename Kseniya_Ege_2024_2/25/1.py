import fnmatch
for x in range(2023, 10 ** 8, 2023):
    if fnmatch.fnmatch(str(x), '3?1*57'):
        print(x, x // 2023)