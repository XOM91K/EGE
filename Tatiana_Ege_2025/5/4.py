# for N in range(1, 1000):
#     R = bin(N)[2:]
#     if N % 2 == 0:
#         R = '11' + R
#     else:
#         R = '1' + R + '10'
#     R = int(R, 2)
#     print(bin(R)[2:], R, N)
print(int('1' + bin(567891233)[2:] + '10',2))