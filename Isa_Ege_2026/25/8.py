def dels(d):
    dell=[]
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            if str(x)[-1] == '9' and x != 9:
                dell.append(x)
            if str(d // x)[-1] == '9' and (d // x) != 9:
                dell.append(d // x)
    return sorted(set(dell))
for x in range(800_001, 100_000_000):
    l=dels(x)
    if len(l)>0:
        print(x, min(l))