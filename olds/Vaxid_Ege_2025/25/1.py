import fnmatch # file name match
for x in range(1917, 10 ** 10, 1917):
    #if d[0] == '3' and d[2:4] == '12' and d[5:7] == '14' and d[-1] == '5':
    if fnmatch.fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)