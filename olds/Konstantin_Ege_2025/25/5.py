import fnmatch
for x in range(10 ** 8 + 1):
    if fnmatch.fnmatch(str(x), '1?58*129'):
        if (x % 117 == 0 and x % 119 != 0 and x % 121 != 0) or \
            (x % 117 != 0 and x % 119 == 0 and x % 121 != 0) or \
            (x % 117 != 0 and x % 119 != 0 and x % 121 == 0):
            print(x, x / 117, x / 119, x / 121)