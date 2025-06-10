def dls(d):
    dels = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            if x % 2 == 0:
                dels.append(x)
            if d // x % 2 == 0:
                dels.append(d // x)
    dels = sorted(dels)
    return dels


for x in range(95632,95700):
    R = dls(x)
    if len(R) == 6:
        print(*R)