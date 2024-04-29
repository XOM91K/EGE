import fnmatch
#6039 на полякове
for x in range(10 ** 8):
    if fnmatch.fnmatch(str(x), '1?58*129'):
        dl = 0
        k = 0
        if x % 117 == 0:
            k += 1
            dl = 117
        if x % 119 == 0:
            k += 1
            dl = 119
        if x % 121 == 0:
            k += 1
            dl = 121
        if k == 1:
            print(x, x // dl)
