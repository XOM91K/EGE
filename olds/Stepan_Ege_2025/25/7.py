import fnmatch
for x in range(123456789, 10 ** 14, 123456789):
    if fnmatch.fnmatch(str(x), '7?3?5*9'):
        d = str(x)
        #if d.count('0') == 5 or  d.count('1') == 5 or
        can = False
        for y in '0123456789':
            if d.count(y) == 5:
                can = True
        if can == True:
            print(x, x // 123456789)