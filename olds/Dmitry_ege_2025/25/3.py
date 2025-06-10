import fnmatch
for x in range(2023, 10 ** 10, 2023):
    if fnmatch.fnmatch(str(x), '1?1?1?1*1'):
        if sum(map(int, str(x))) == 22:
            print(x, x // 2023)