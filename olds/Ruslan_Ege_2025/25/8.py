import fnmatch
for x in range(123456789, 10 ** 14, 123456789):
    if fnmatch.fnmatch(str(x), '7?3?5*9'):
        can = False
        for y in str(x):
            if str(x).count(y) == 5:
                can = True
                break
        if can:
            print(x, x // 123456789)