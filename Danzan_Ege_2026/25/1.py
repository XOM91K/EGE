import fnmatch
for x in range(2024, 10 ** 10 + 1, 2024):
    if fnmatch.fnmatch(str(x), '3?2258*4'):
        print(x)