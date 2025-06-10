#https://examinf.ru/tasks/912
def is_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return n > 1
def dels(n):
    dls = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            if is_prime(x):
                dls.append(x)
            if is_prime(n // x):
                dls.append(n // x)
    return sorted(set(dls))
ct = 0
for x in range(1_000_001, 10 ** 10):
    dls = dels(x)
    if len(dls) == 3:
        print(x, max(dls))
        ct += 1
        if ct == 5:
            break