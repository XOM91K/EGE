import fnmatch
for x in range(98591, 10 ** 12 + 1, 98591):
    if fnmatch.fnmatch(str(x), "12?3*456??9"):
        print(x, x // 98591)
