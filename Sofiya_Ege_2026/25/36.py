def dels(d):
    l=[]
    for x in range(1, int(d**0.5)+1):
        if d%x==0:
                l.append(x)
                l.append(d//x)
    return sorted(set(l))
# 2 ^ m * p ^ 4
d = []
for m in range(1, 27):
    for p in range(1, 100):
        x = 2 ** m * p ** 4
        if 55_000_000 <= x <= 60_000_000:
            l=dels(x)
            nch=[x for x in l if x%2!=0]
            if len(nch)==5:
                if [x, max(nch)] not in d:
                    d.append([x, max(nch)])
d = sorted(d)
for x in d:
    print(*x)
# for x in range(55_000_000, 60_000_000):
#     l=dels(x)
#     nch=[x for x in l if x%2!=0]
#     if len(nch)==5:
#         print(x, max(nch))