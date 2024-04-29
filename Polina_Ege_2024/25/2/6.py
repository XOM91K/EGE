import fnmatch
def dels(n):
    l = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
    return sorted(set(l))
for x in range(1, 31622):
    x **= 2
    d = dels(x)
    if len(d) == 9 and fnmatch.fnmatch(str(x), '15*3*09'):
        print(x, d[-2])