def dels(n):
    dels = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0 and x != n // x:
            dels.append(x)
            dels.append(n // x)
        elif n % x == 0:
            dels.append(x)
    return sorted(dels)
for x in range(185311, 185331):
    if len(dels(x)) == 4:
        print(dels(x))