def v5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
l = []
for N in range(5, 10000):
    R = v5(N)
    if N % 5 == 0:
        R = R + R[-2:]
    else:
        R = R + v5(N % 5 * 7)
    R = int(R, 5)
    if R > 200:
        l.append(R)
print(min(l))
# s = 'ЯБЛОКО'
# print(s[:2])
# print(s[-2])
# print(s[:-2])
# print(s[-2:])
# d = 5
# if d > 1:
#     print('Привет')
# s = 'ПРИВЕТ'
# s = s + 'Д'
# print(s)