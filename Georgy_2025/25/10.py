import fnmatch
for x in range(2023, 10 ** 9, 2023):
    sc = sum(map(int, str(x)))
    #if sc % 7 == 0 and sc < 20 and str(x)[:2] == '20' and str(x)[-2:] == '23':
    if sc % 7 == 0 and sc < 20 and fnmatch.fnmatch(str(x), '20*23'):
        print(x, x // 2023)