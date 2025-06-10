ct = 0
for A in range(-300, 300):
    can = True
    for x in range(-300, 300):
        for y in range(-300, 300):
            if (((A < x) or (x**2 - 7*x + 10 > 0)) and ((A >= y) or ((y ** 2 + 7*y + 12) > 0))) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)
        ct+=1
print(ct)