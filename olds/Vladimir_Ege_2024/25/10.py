import fnmatch
for x in range(17, 10 ** 9, 17):
    if fnmatch.fnmatch(str(x), '1?34567?9'):
        print(x, x // 17)