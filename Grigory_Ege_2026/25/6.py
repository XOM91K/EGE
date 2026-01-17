def dels(d):
    l = []
    for x in range(2,int(d**0.5)+1):
        if d % x == 0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for a in range(18782,18823):
    ncht = [y for y in dels(a) if y % 2 != 0]
    if len(ncht) == 3 :
        print(*ncht)