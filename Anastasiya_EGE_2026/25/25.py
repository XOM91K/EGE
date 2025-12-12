import fnmatch
for x in range(27919, 10**14+1, 27919):
    s = str(x)
    if s[:3] == '125' and s[6:9] == '125' and s[-3:] == '554':
    #if fnmatch.fnmatch(str(x), '125???125**554'):
    # for z1 in range(10):
    #     for z2 in range(10):
    #         for z3 in range(10):
    #             for ww in range(0, 100):
    #
        print(x, x//27919)