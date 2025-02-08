import math
l = []
for n in range(4, 10000):
    s = '2' + '7' * n
    while '27' in s or '777' in s or '377' in s:
        if '27' in s:
            s = s.replace('27', '7', 1)
        if '777' in s:
            s = s.replace('777', '3', 1)
        if '377' in s:
            s = s.replace('377', '72', 1)
            #1233
    # m = (s.count('1') * 1 * s.count('2') * 2 * s.count('3') * 3 * s.count('4') * 4 * s.count('5') * 5 * s.count(
    #     '6') * 6 * s.count('7') * 7 * s.count('8') * s.count('9') * 9)
    sm = math.prod(map(int, s))
    if sm % 3 == 0 and str(sm)[-1] == '1':
        l.append(n)
print(max(l))
# import math
# f = '1233'
# print(math.prod(map(int, f)))
# pr = 1
# for x in f:
#     pr *= int(x)
# print(pr)