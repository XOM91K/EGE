import fnmatch
def dels(d):
    dls = []
    for x in range(2,int(d ** 0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
            break
    return sorted(set(dls))
for x in range(1945,10**10,1945):
    dls = dels(x)
    x =str(x)
    # if x[0] == '6' and x[2:4] == '38' and x[-3] == '9' and x[-1] == '5':
    if fnmatch.fnmatch(x,'6?38*9?5'):
        M = dls[0] + dls[-1]
        if str(M)[-3:] == '792':
            print(x,sum(map(int,str(M))))