import fnmatch
for x in range(27919, 10**14 ,27919):
    if fnmatch.fnmatch(str(x), '125???125**554'):
        print(x, x//27919)