import fnmatch
for x in range(2024, 10 ** 10, 2024):
    if fnmatch.fnmatch(str(x), '1?2*4'):
        if x ** 0.5 % 1 == 0:
            print(x, x // 2024)