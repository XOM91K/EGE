import fnmatch
def dels(x):
    c = []
    for d in range(1,int(x**0.5)+1):
        if x%d == 0:
            if fnmatch.fnmatch(str(d),'2*3?'):
                c.append(d)
            if fnmatch.fnmatch(str(x // d), '2*3?'):
                c.append(x // d)
    if len(c) != 0:
        print(x,min(c))
    else:
        return 0
for x in range(500_000,550_000):
    dels(x)