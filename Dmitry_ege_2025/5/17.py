mn = 10000000
for N in range(1, 10000):
    R = bin(N)[2:]
    if len(R) % 2 == 0:
        R = R + '1'
    else:
        R = '1' + R + '0'
    R = int(R, 2)
    if R > 666:
        mn = min(R, mn)
print(mn)

# R = '1010101010101010101010101010101010101111111111901271209317cn0UASGA*(d&asdastda*&wdta&*sdrs*&dsdrs^&dsdrs*ds*111111111111111'
# print(R.count('1') + R.count('0'))
# print(len(R))
# import random
# mn = 1000000000000000000000000000000
# mx = -100000000
# for x in range(1, 100000):
#     x = random.randint(1000, 100000)
#     if (x % 7 == 0 and x % 2 == 0 and x % 4 == 0 and x % 32 == 0):
#         mn = min(mn, x)
#         mx = max(mn, x)
# print(mn, mx)