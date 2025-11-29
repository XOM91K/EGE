import fnmatch
for x in range(12312312, 10**14, 12312312):
    if fnmatch.fnmatch(str(x), '???6*'):
        x = str(x)
        if x == x[::-1]: # abccba
            print(x, int(x) // 12312312)