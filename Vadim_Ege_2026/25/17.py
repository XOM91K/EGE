import fnmatch
for x in range(123456789, 10 ** 14, 123456789):
    s = str(x)
    s = [s.count(x) for x in s]
    if 5 in s and fnmatch.fnmatch(str(x), '7?3?5*9'):
        print(x, x // 123456789)