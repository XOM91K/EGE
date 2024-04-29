import fnmatch
def dels(n):
    dels = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            dels.append(x)
            dels.append(n // x)
    return sorted(set(dels))
ct = 0
for x in range(500_001, 500_001 * 2):
    if fnmatch.fnmatch(str(sum(dels(x))), '*7?'):
        print(x, sum(dels(x)))
        ct += 1
    if ct == 5:
        break