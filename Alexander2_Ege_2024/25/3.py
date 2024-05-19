import fnmatch
for x in range(10 ** 8):
    sm_nch = sum([int(d) for d in str(x) if int(d) % 2 != 0])
    if fnmatch.fnmatch(str(x), '124*5*79'):
        if x % sm_nch == 0:
            print(x, sum(map(int, str(x))))