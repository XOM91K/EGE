import fnmatch
for x in range(4329, 10**10 + 1, 4329):
    if fnmatch.fnmatch(str(x), '1*1298*6'):
        print(x, x // 4329)