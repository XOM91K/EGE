def v9(d):
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    return s[::-1]
n = 19 ** 81 + 23 ** 709 - 4
n = v9(n)
ct = 0
for i in range(1, 8):
    ct += n.count('8' + str(i))
print(ct)