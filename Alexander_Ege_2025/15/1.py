#https://examinf.ru/tasks/147
for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((A + x < 123) <= ((x % 5 == 0) <= (x % 7 != 0))) == 0:
            can = False
            break
    if can:
        print(A)