def dels(n):
    dls = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if str(x)[-1] == '9' and x != 9:
                dls.append(x)
            if str(n // x)[-1] == '9':
                dls.append(n // x)
    return sorted(set(dls))

for x in range(800_001, 10 ** 10):
    d = dels(x)
    if len(d) > 0:
        print(x, min(d))
    # if d[-1] == '9':
    #     print(x, d)