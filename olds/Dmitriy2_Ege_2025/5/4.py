for N in range(1, 10000):
    R = bin(N)[2:]
    # 10101
    if R.count('1') % 2 != 0:
        R = R + '11'
    else:
        R = '11' + R
    R = int(R, 2)
    if R > 102:
        print(N)
# s = 'ОБР'
# s = s + 'УЧ'
# print(s)
# s = 'ТО'
# s = 'ЛЕ' + s
# print(s)