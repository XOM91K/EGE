#№ 18877 (Уровень: Базовый)
for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (not((x < 7) or (y >= 5 * x + A - 60) or (x >= 36) or (y < 225))) == 1:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)