def is_prime(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return x > 1
def M(d):
    l=[]
    for x in range(2, int(d**0.5)+1):
        if d%x==0:
            if is_prime(x):
                l.append(x)
            if is_prime(d // x):
                l.append(d//x)
    return sorted(set(l))
for x in range(1_200_001, 10**10):
    M3 = M(x)
    if len(M3) > 0:
        M3 = M3[0] + M3[-1]
    else:
        M3 = 0
    if M3>2000 and M3%10==8:
            print(x, M3)