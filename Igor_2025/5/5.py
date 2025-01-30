for N in range(132217759, 134217760):
    R = bin(N)[2:]
    R = bin(R.count('1'))[2:] + bin(R.count('0'))[2:]
    R = int(R, 2)
    if R == 214:
        print(N)
        break
print(bin(214)[2:])
# #единицы потом нули
# #110  10110
# #6    22
# print(int('10110', 2))
# print('1' + '0' * 22 + '1' * 5)
# print(int('1000000000000000000000011111', 2))