import fnmatch
for x in range(23, 10**6, 23):

            if fnmatch.fnmatch(str(x), "#6215"):
                print(x, x // 23)