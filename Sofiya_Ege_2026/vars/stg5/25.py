def is_prime(d):
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            return False
    return d>1
def dels(d):
    l=[]
    l2 = []
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            l.append(x)
            l.append(d // x)
            if is_prime(x):
                l2.append(x)
            if is_prime(d//x):
                l2.append(d//x)
    return [sum(set(l)), len(set(l2))]
for n in range(4_555_706, 10 ** 7):
    if str(n)[-1] != '3':
        S, K = dels(n)
        if abs(S + K - n) % 100 == 23:
            print(n)
            # 4555900
            # 4555902
            # 4556054
            # 4556805
            # 4557198