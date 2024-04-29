def prime(n):
    if n == 1:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
def dels(n):
    l = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            if prime(x):
                l.append(x)
            if prime(n // x):
                l.append(n // x)
    return sorted(l)
ct = 0
for x in range(2, 20001):
    d = dels(x)
    if len(d) > 3:
        ct += 1
print(ct)