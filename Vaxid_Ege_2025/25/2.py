import fnmatch
for x in range(2023, 10 ** 9, 2023):
    if fnmatch.fnmatch(str(x), '20*23'):
        if sum(map(int, str(x))) % 7 == 0 and sum(map(int, str(x))) < 20:
            print(x, x // 2023)