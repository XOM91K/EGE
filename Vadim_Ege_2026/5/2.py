minim = 100000
for N in range(0, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:  ##
        R = R + '0'
    else:
        R = R + '1'
    if bin(N)[2:].count('1') % 2 == 0:  ##
        R = R + '0'
    else:
        R = R + '1'
    R = int(R, 2)
    if R < minim and R > 2023:  ##
        minim = R
print(minim)  # выводит неверный ответ, скорее всего накосячил в помеченных строчках
