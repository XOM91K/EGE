import fnmatch
for x in range(2023, 10 ** 9 + 1, 2023):
    if fnmatch.fnmatch(str(x), '20*23'):
        if sum(map(int, str(x))) in [0, 7, 14]:
            print(x, x // 2023)