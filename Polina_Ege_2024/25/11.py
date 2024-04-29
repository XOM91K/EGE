import fnmatch
for x in range(79, 10 ** 8 + 1, 100):
    sm_nch = 0
    sm = 0
    for y in str(x):
        sm += int(y)
        if int(y) % 2 != 0:
            sm_nch += int(y)
    if x % sm_nch == 0 and fnmatch.fnmatch(str(x), '124*5*79'):
        print(x, sm)