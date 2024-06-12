d = 144
def delss(d):
    dels = []
    for x in range(1, int(d ** 0.5) + 1):
        if d % x == 0:
            dels.append(x)
            dels.append(d // x)
    return sorted(set(dels))
print(delss(d))