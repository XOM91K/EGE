import fnmatch
for x in range(1017, 10 ** 10, 1017):
    if fnmatch.fnmatch(str(x), '2?5432*1'):
        if '9' in str(x):
            print(x, x // 1017)