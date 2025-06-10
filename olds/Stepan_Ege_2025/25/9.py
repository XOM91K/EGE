import fnmatch
for x in range(519, 10 ** 13, 519):
    if fnmatch.fnmatch(str(x), '32*54?123'):
        d = str(x)
        if d.count('0') == 0 and len(d) % 2 == 0:
            print(x, x // 519)