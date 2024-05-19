def dels(d):
    dl = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dl.append(x)
            dl.append(d // x)
    return sorted(set(dl))
print(dels(16))