import fnmatch
for x in range(2023, 10 ** 9, 2023):
    if fnmatch.fnmatch(str(x), '20*23'):
        sm = sum(map(int, str(x)))
        if sm % 7 == 0 and sm < 20:
            print(x, x // 2023)