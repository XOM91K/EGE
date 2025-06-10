def v6(d):
    s = ''
    while d > 0:
        s += str(d % 6)
        d //= 6
    return s[::-1]
for N in range(1, 10000):
    R = v6(N) #967
    if N % 3 == 0:
        R += R[:2]
    else:
        R += v6(N % 3 * 10)
    R = int(R, 6)
    if R > 680:
        print(R)
# s = 'Привет'
# print(s[2:])
# print(s[5:])
# print(s[:9])
# print(s[:2])

s = 'СОЛНЫШКО'
# s[start_index:finish_index:step]
# s[1:5:1]
print(s[0:2])
print(s[::-1])
print(s[-4:])
print(s[1:5:1])
print(s[1:5:2])
print(s[0:4])
print(s[:4])