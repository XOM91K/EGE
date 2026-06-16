def v4(d):
    s = ''
    while d > 0:
        s += str(d % 4)
        d //= 4
    return s[::-1]
print(v4(2026))
#
# for x in range(1, 1000):
#     R = v7(x)
#     if x % 2 == 0:
#         R = '52' + R + '1'
#     else:
#         R = R[-1] + R[1:-1] + R[0] + '15'
#     #R = int(R, 7)
#     if len(str(int(R))) == 4:
#         print(x)
