def dels(n):
    l = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
    return sorted(set(l))
mx = 0
dl = []
for x in range(394441, 394506):
    d = dels(x)
    if len(d) > mx:
        dl.append([len(d), x])
        mx = len(d)
print(dl)