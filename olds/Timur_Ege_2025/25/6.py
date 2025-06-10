import fnmatch
for x in range(123456789, 10 ** 14, 123456789):
    s = str(x)
    if fnmatch.fnmatch(s, '7?3?5*9'):
        if s.count('1') == 5 or s.count('2') == 5 or s.count('3') == 5 or s.count('4') == 5 or s.count('5') == 5 or s.count('6') == 5 or s.count('7') == 5 or s.count('8') == 5 or s.count('9') == 5:
            print(x, x // 123456789)
