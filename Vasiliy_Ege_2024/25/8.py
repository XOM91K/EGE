import fnmatch
for x in range(28, 10 ** 9, 28):
    if fnmatch.fnmatch(str(x), '6323*353?'):
        print(x, x // 28)