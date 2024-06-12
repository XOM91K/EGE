import fnmatch
for n in range(4329, 10**10, 4329):
    if fnmatch.fnmatch(str(n), '1*1298*6'):
        print(n, int(n) // 4329)