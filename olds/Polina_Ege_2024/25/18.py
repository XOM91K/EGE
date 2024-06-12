import fnmatch
for x in range(685, 10 ** 7, 685):
    if fnmatch.fnmatch(str(x), '23*61*5'):
        print(x, x // 685)