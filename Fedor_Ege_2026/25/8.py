def dels(n):
    dls = []
    for x in range(1, int(n**0.5)+1):
        dls.append(x)
        dls.append(n//x)
    return sorted(set(dls))
for d in range(1000, 10000):
    f = dels(d)
    s = sum(f)
    if str(s)[-2:] == '23':
        print(d, s)