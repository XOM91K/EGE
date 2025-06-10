import fnmatch
for x in range(2024, 10 ** 10, 2024):
    if fnmatch.fnmatch(str(x), '112?57*4') and sum(map(int, str(x))) % 2 != 0:
            print(x, x // 2024)