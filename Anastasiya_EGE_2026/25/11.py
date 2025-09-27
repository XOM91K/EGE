import fnmatch
for x in range(123456789, 10 ** 14 + 1, 123456789):
    if fnmatch.fnmatch(str(x), '7?3?5*9'):
        #f len(str(x)) - len(set(str(x))) >= 4:i
        for y in '0123456789':
            if str(x).count(y) == 5:
                print(x, x // 123456789)
                break