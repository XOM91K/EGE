def dels(n):
    l = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
    return sorted(set(l))
ct = []
import fnmatch
for n in range(31622 + 1, 50000):
    d = n ** 2
    if len(dels(d)) == 45 and fnmatch.fnmatch(str(d), '1*2*7*04'):
        ct.append([d, dels(d)[-2]])
        if len(ct) == 5:
            break
print(sorted(ct))