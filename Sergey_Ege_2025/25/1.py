import fnmatch
for x in range(161, 10 ** 8, 161):
    if fnmatch.fnmatch(str(x), '12*4?65'):
        print(x, x // 161)