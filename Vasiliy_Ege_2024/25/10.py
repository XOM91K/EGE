import fnmatch
for x in range(4013, 10 ** 12, 4013):
    if fnmatch.fnmatch(str(x), '123?4*5679'):
        print(x, x // 4013)