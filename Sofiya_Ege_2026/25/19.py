import fnmatch
for x in range(12312312, 10**14, 12312312):
    if fnmatch.fnmatch(str(x), '???6*'):
        if str(x) == str(x)[::-1]:
            print(x, x//12312312)