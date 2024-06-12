import fnmatch
def dels(d):
    dl = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dl.append(x)
            dl.append(d // x)
    return sorted(set(dl))

for x in range(2024, 10 ** 8, 2024):
        if fnmatch.fnmatch(str(x - 1), '13*7?5'):
            print(x - 1, dels(x - 1)[-2])