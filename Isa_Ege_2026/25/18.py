def is_prime(d):
    for x in range(2, int(d**0.5)+1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    dls = []
    for x in range(1, int(d**0.5)+1):
        if d % x == 0:
            if '3' in str(x) and '5' in str(x) and is_prime(x):
                dls.append(x)
            if '3' in str(d//x) and '5' in str(d//x) and is_prime(d//x):
                dls.append(d//x)
    return sorted(set(dls))
# 3_600_001 1897
for x in range(4081477, 4_500_000):
    l = dels(x)
    if (len(l) == 3 and l[0] * l[1] * l[2] == x) or (len(l) == 2 and l[0] * l[0] * l[1] == x) or (len(l) == 2 and l[0] * l[1] * l[1] == x):
        print(x, max(l), l)
4081477 1453
4278107 1523
4300579 1531
4334287 1543
4362377 1553