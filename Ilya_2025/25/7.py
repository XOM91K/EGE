import math
def dels(n):
    dl = []
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            dl.append(x)
            dl.append(n // x)
    dl = sorted(set(dl))
    return dl
ct = 0
for x in range(800_001, 900_000):
    dl = dels(x)
    if len(dl) >= 2:
        M = dl[0] + dl[-1]
        if M % 10 == 4:
            print(x, M)
            ct += 1
        if ct == 5:
            break