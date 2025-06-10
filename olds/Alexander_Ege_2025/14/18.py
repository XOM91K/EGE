def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
mx_nol = 0
mx_x = 0
for x in range(1, 2031):
    c = 7 ** 170 + 7 ** 100 - x
    c = v7(c)
    if c.count('0') > mx_nol:
        mx_nol = c.count('0')
        mx_x = x
print(mx_x)
