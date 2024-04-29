import fnmatch
ct = 0
for x in range(73, 10 ** 10, 73):
    if fnmatch.fnmatch(str(x), '12345*76'):
        ct += 1
        print(x, x // 73)
    if ct == 5:
        break