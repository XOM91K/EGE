import fnmatch
for x in range(7423, 10 ** 10, 7423):
    if fnmatch.fnmatch(str(x), '4*4736*1'):
        print(x, x // 7423)