def f(n, m):
    if n%m==0:
        return True
    else:
        return False
ct = 0
for a in range(1, 1001):
    can = True
    for x in range(1, 10000):
        if (f(a, 35) and (f(730, x) <= ((not f(a, x)) <= ((not f(110, x)))))) == 0:
            can = False
    if can:
        print(a)
        ct += 1
print(ct)