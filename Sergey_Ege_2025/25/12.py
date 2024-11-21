def dls(d):
    dels = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dels.append(x)
            dels.append(d // x)
    dels = sorted(dels)
    if len(dels) == 2:
        return 0
    return dels[1] + dels[-2]


ct = 0
for x in range(900000, 18000000, 1):
    M = str(dls(x))
    if M[-2:] == "46":
        print(x, M)
        ct += 1
    if ct == 5:
        break
    # M = int(M_real[0] + M_real[-1])

    #   print(x,M)
