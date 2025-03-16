import fnmatch
for x in range(2627, 10 ** 9, 2627):
    if fnmatch.fnmatch(str(x), '7*53?3*1'):
        if sum(map(int,str(x))) in [29, 31, 37, 41, 43, 47]:
            print(x, x // 2627)