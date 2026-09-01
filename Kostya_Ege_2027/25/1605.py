def dels(d):
    l = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return len(sorted(set(l)))
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
ll = []
for x in range(3163, 7746):
    x = x ** 2
    dl = dels(x)
    if is_prime(dl):
        ll.append([x, dl])
print(sorted(ll, key=lambda d: -d[1])[:7])
for x in sorted(ll, key=lambda d: -d[1])[:7]:
    print(*x)