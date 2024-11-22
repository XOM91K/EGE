# for i in range(1580 - 45):
#     for j in range(i + 37, i + 45 ):
#
#
sl = {}
for x in range(1, 2000):
    s = '1' * x + '5' + '1' * 40 + '5' + '1' * x
    while '111' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '15', 1)
        else:
            s = s.replace('111', '51', 1)
    print(x, s)