def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if str(x)[-1] == '9' and x != 9:
                dls.append(x)
            if str(d // x)[-1] == '9':
                dls.append(d // x)
    return sorted(set(dls))
for N in range(800_001, 10 ** 6):
    dls = dels(N)
    if len(dls) > 0:
        print(N, min(dls))
