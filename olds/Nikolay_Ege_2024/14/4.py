for x in range(22):
    c1 = 1 * int(str('132'+str(x)+'4')) + 3
    c2 = int('13' + str(x) + '42', 22)
    if abs(c1 - c2) % 100 == 53:
        print(x, abs(c1 - c2) // 100)