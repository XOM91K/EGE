def t(n):
    s = ''
    while n > 0:
         s = str(n % 3) + s
         n //= 3
    return s
for N in range(1, 10000):
    R = t(N)
    if sum(map(int, R)) % 3 == 0:
        R = '20' + R
    else:
        R = '10' + R
    R = int(R, 3)
    if R < 100:
        print(N)
# d = '231' #6
# sm = 0
# for x in d:
#     sm += int(x)
# print(sm)
# # print(sum(map(int, d)))