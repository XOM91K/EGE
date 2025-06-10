import fnmatch
for x in range(10 ** 8):
    if fnmatch.fnmatch(str(x), '*15*7424'):
    #if str(x)[-4:] == '7424' and '15' in str(x)[:-4]
        k = 0
        t = 0
        if x % 113 == 0:
            k += 1
            t = 113
        if x % 111 == 0:
            k += 1
            t = 111
        if x % 127 == 0:
            k += 1
            t = 127
        if k == 1:
            print(x, x // t)