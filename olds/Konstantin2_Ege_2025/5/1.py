for N in range(1, 10000):
    R = bin(N)[2:]
    R = R + str(R.count('1') % 2)
    R = R + str(R.count('1') % 2)
    R = int(R, 2)
    if R > 125:
        print(N, R)
        break
#срезы
# s = 'ХЛЕБ'
# print(s[::-1])
# s = 'ОЛОЛО'
# print(s.count('ЛО'))
# print(17 % 10)
# print(14 % 8)
# print(14 % 6)