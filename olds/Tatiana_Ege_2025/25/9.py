def deli(x):
    d = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)
    return sorted(set(d))

for i in range(0, 10 ** 9 , 106):
    d = deli(i)
    if len(d) == 7:
        print(i, max(d))