def dels(d):
    l = []
    for x in range(1,int((d ** 0.5))+1):
        if d % x == 0:
            if is_prime(x):
                l.append(x)
            if is_prime(d // x):
                l.append(d//x)
    return sorted(set(l))
def is_prime(d):
    for x in range(2,int(d**0.5)+1):
        if d % x == 0 :
            return False
    return d > 1
M = 0
for x in range(5700000,10**9):
    s = dels(x)
    if len(s) > 1:
        M = s[0] + s[-1]
        if M > 70_000 and M ** 0.5 % 1 == 0:
                print(x, M)