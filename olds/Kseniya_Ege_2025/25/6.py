import fnmatch
for x in range(2627, 10 ** 9, 2627):
    if fnmatch.fnmatch(str(x), '7*53?3*1'):
        sm = sum(map(int, str(x)))
        if sm == 29 or sm == 31 or sm == 37 or sm == 41 or sm == 47 or sm == 43:
            print(x, x // 2627)