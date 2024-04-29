import fnmatch

def dels(n):
    dl = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dl.append(i)
            dl.append(n // i)
    return sum((set(dl)))
ct = 0
for x in range(500001, 5000000):
    if fnmatch.fnmatch(str(dels(x)), '*7?'):
        print(x, dels(x))
        ct += 1
    if ct == 5:
        break
