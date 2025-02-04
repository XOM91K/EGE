import fnmatch
chet = []
def dels(d):
    dls = []
    for y in range(1, int(d ** 0.5) + 1):
        if d % y == 0:
            if y % 2 == 0:
                dls.append(y)
            if (d // y) % 2 == 0:
                dls.append(d // y)
    return sorted(set(dls))
for x in range(65000,10**9):
    if fnmatch.fnmatch(str(x),'6*97*5?'):
        if len(dels(x)) >= 4:
           print(x,sum(dels(x)))