import fnmatch
for x in range(9573, 10 ** 10 + 1, 9573):
    if fnmatch.fnmatch(str(x), '202*47*6'):
        print(x, x // 9573)