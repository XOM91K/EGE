def dels(n): #ВОЗВРАЩАЕТ СПИСОК ДЕЛИТЛЕЙ ЧИСЛА
    dl = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            dl.append(x)
            dl.append(n // x)

    return list(set(dl))
ct = 0
for x in range(860_000, 1000_000):
    d = dels(x)
    if len(d) != 0:
        sm = max(d) + min(d)
        if sm % 100 == 18:
            print(x, sm)
            ct += 1
        if ct == 5:
            break