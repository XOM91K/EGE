def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
def dels(d):
    dls = []
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            if is_prime(x) and str(x).count('1') == 1: #делитель проверяем (левый)
                dls.append(x)
            if is_prime(d // x) and str(d // x).count('1') == 1: #делитель проверяем (правый)
                dls.append(d // x)
    return sorted(set(dls))
for t in range(3_000_001, 10 ** 10):
    g = dels(t)
    if len(g) == 2: #Ровно два простых делителя, у которых есть одна единица
        print(t, sum(g))

        