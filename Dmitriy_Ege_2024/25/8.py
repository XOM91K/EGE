import fnmatch
for x in range(2025, 10 ** 8 + 1, 2025):
    if fnmatch.fnmatch(str(x), "12*34?5"):
        print(x, x // 2025)
