import fnmatch
for x in range(1923, 10 ** 8 + 1, 1923):
    x = str(x)
    if fnmatch.fnmatch(x, "1*2??76"):
        print(x, int(x) // 1923)