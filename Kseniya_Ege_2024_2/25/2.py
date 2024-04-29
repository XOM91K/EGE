import fnmatch
for x in range(2024, 10 ** 10, 2024):
    if fnmatch.fnmatch(str(x), '1?2157*4'):
        print(x, x // 2024)