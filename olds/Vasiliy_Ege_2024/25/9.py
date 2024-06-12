import fnmatch
for x in range(5321, 10 ** 10, 5321):
    if fnmatch.fnmatch(str(x), '12*135*9'):
        print(x, x // 5321)