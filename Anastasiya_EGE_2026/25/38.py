def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x) and ('3' in str(x) or '7' in str(x)):
                dls.append(x)
            if is_prime(d // x) and ('3' in str(d // x) or '7' in str(d // x)):
                dls.append(d // x)
    return sorted(set(dls))
import itertools, math
for x in range(5_000_001, 10 ** 7):
    dls = dels(x)
    if len(dls) > 0:
        d = itertools.product(dls, repeat=3)
        for tup in d:
            if math.prod(tup) == x:
                print(x, tup)
                break