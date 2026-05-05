def is_prime(d):
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            return False
    return d>1
def dels(d):
    l=[]
    for x in range(1, int(d**0.5)+1):
        if d%x==0:
            if is_prime(x):
                if str(x).count('3')>0 and str(x).count('5')>0:
                    l.append(x)
            if is_prime(d//x):
                if str((d//x)).count('3') > 0 and str((d//x)).count('5') > 0:
                    l.append(d//x)
    return sorted((l))
for x in range(4_000_001, 10**7):
    l=dels(x)
    if len(l)==2 and (l[0] * l[0] * l[1] == x or l[1] * l[1] * l[0] == x):
            print(x, max(l))