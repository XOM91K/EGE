# def dels(n):
#     dls = []
#     for x in range(2, n):
#         if n % x == 0:
#             dls.append(x)
#     return dls
def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dls.append(x)
            dls.append(n // x)
    return sorted(set(dls))
ct = 0
for x in range(900_001, 10 ** 10):
    dls = dels(x)
    M = 0
    if len(dls) >= 2:
        M = dls[0] + dls[-1]
    if str(M)[-2:] == '46':
        print(x, M)
        ct = ct + 1
    if ct == 5:
        break