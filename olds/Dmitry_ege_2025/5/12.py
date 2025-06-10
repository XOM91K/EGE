for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('0') > 0:
        ind = R.rindex('0')
        R = R[:ind] + R[:2] + R[ind + 1:]
        R = R[::-1]
        if int(R, 2) == 123:
            print(N)
# d = 'КАРТОШКАГОД'
# #последнюю букву А заменить на первые три символа слова
# ind = d.rindex('А')
# d = d[:ind] + d[:3] + d[ind + 1:]
# print(ind, d)