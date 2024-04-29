import fnmatch
for x in range(1, 10**8):
    p = 0
    if x % 117 == 0:
        p += 1
    if x % 119 == 0:
        p += 1
    if x % 121 == 0:
        p += 1
    if p == 1:
        if fnmatch.fnmatch(str(x), '1?58*129'):
            p = 0
            if x % 117 == 0:
                p = 117
            if x % 119 == 0:
                p = 119
            if x % 121 == 0:
                p = 121
            print(x, x // p)