import fnmatch
for x in range(519, 10**13, 519):
    if len(str(x)) % 2 == 0 and '0' not in str(x):
        if sum(map(int, str(x)[:len(str(x)) // 2])) == sum(map(int, str(x)[len(str(x)) // 2:])):
            if fnmatch.fnmatch(str(x), "32*54?123"):
                print(x, x // 519)