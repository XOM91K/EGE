l = []
for n in range(4, 10000):
    s = '4' + '1' * n
    while '411' in s or '1111' in s:
        if '411' in s:
            s = s.replace('411', '14', 1)
        if '1111' in s:
            s = s.replace('1111', '1', 1)
    l.append(sum(map(int, s)))
print(max(l))
# print(sum('123'))
# print(sum(123))
# s = '1832189123983126321983216831293612392136129319' #21
# print(s.count('1') * 1 + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9)
# print(sum(map(int, s)))
# summapint