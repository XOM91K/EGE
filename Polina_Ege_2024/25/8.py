import fnmatch
def dels(n):
    dels = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            dels.append(x)
            dels.append(n // x)
    return list(set(dels))
for x in range(53, 10 ** 7 + 1, 53):
    if fnmatch.fnmatch(str(x), '*2?2*'):
        if str(x) == str(x)[::-1]:
            if len(dels(x)) > 30:
                print(x, sum(dels(x)))