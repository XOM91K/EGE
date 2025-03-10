for N in range(1, 10000):
    R = bin(N)[2:]
    if '0' in R:
        ind = R.rindex('0')
        R = R[:ind] + R[:2] + R[ind + 1:]
        R = R[::-1]
        R = int(R, 2)
        if R == 123:
            print(N)
# R = '101010111'
# ind = R.rindex('0')
# R = R[:ind] + R[:2] + R[ind + 1:]
# print(ind)
# print(R)
# #В этой записи последний ноль заменяется
# # на первые две цифры полученной записи.
# # 10101 10 111
