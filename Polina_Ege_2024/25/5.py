import fnmatch
for x in range(19 * 6 * 2023, 999999999, 19 * 6 * 2023):
    if fnmatch.fnmatch(str(x), '1*1*1?'):
        print(x, x // 2023)