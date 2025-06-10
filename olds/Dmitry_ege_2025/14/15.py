cts = 0
def v9(x):
    s = ''
    while x > 0:
        s += str(x % 9)
        x //= 9
    return s[::-1]
for x in range(1, 10000):
    d = 9 ** 1942 + 9 * 6 ** 971 + 214 - x
    d = v9(d)
    if abs(d.count('2') - d.count('8')) == 471:
        print(x)
# d = -9
# print(abs(d))