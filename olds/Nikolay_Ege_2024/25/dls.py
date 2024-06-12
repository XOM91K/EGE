def dels(n): #ВОЗВРАЩАЕТ СПИСОК ДЕЛИТЛЕЙ ЧИСЛА
    dl = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            dl.append(x)
            dl.append(n // x)
    return list(set(dl))