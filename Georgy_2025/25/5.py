#https://examinf.ru/tasks/913
def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    dls = sorted(set(dls))
    if len(dls) > 0:
        M = dls[0] + dls[-1]
    else:
        M = 0
    return M

ct = 0
for x in range(900_001, 10 ** 10):
    M = dels(x)
    if str(M)[-2:] == '46':
        print(x, M)
        ct += 1
        if ct == 5:
            break