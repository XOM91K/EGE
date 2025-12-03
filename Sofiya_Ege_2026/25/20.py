import fnmatch
for x in range(123456789, 10**14, 123456789):
    if fnmatch.fnmatch(str(x), '7?3?5*9'):
        flag = False
        for y in '0123456789':
            if str(x).count(y) == 5:
                flag = True
                break
        if flag == True:
            print(x, x//123456789)