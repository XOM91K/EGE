def v9(d):
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    return s[::-1]
ct = 0
for x in range(1,8):
    f = 19 ** 81 + 23 ** 709 - 4
    R = v9(f)
    ct += R.count('8' + str(x))
print(ct)