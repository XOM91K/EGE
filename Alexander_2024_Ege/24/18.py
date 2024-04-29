import fnmatch, itertools
def prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
def dels(n):
    prime_dl = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if prime(x):
                prime_dl.append(x)
            if prime(n // x):
                prime_dl.append(n // x)
    return list(set(prime_dl))
for i in range(1,10**4):
    if fnmatch.fnmatch(str(i),"*2?2"):
        g = dels(i)
        for j in itertools.product(g, repeat=7):
            if j[0] * j[1] * j[2] * j[3] * j[4] * j[5] * j[6] == i:
                print(i, max(j))
                break