import fnmatch
for x in range(123456789, 10 ** 14, 123456789):
    if fnmatch.fnmatch(str(x), '7?3?5*9'):
        if str(x).count('1') == 5 or str(x).count('2') == 5 or str(x).count('3') == 5 or str(x).count('4') == 5 or str(x).count('5') == 5 or str(x).count('6') == 5 or str(x).count('7') == 5 or str(x).count('8') == 5 or str(x).count('9') == 5:
        # can = False
        # for s in '123456789':
        #     if str(x).count(s) == 5:
        #         can = True
        # if can:
            print(x,  x // 123456789)