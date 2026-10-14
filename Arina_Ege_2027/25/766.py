import fnmatch
for x in range(1917, 10 ** 10, 1917):
    if x % 1917 == 0:
        if fnmatch.fnmatch(str(x), '3?12?14*5'):
        #s = str(x)
        #if s[0] == '3' and s[2:4] == '12' and s[5:7] == '14' and s[-1] == '5':
            print(x, x // 1917)