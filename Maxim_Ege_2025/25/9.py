def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    dls = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x) == True:
                dls.append(x)
            if is_prime((d // x)) == True:
                dls.append(d // x)
    return sorted((dls))


for x in range(10 ** 6, 10 ** 10):
    if len(dels(x)) == 3:
        print(x, max(dels(x)))

