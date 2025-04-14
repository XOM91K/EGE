import math
for n in range(4, 10000):
    s = '2' + '7' * n
    while '27' in s or '777' in s or '377' in s:
        if '27' in s:
            s = s.replace('27', '7', 1)
        if '777' in s:
            s = s.replace('777', '3', 1)
        if '377' in s:
            s = s.replace('377', '72', 1)
    if math.prod(map(int, s)) % 3 == 0 and str(math.prod(map(int, s)))[-1] == '1':
        print(n)
# s = '121294712598327420812841209523759536790312433' #9
# print(s.count('1') * 1 + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('8') * 8 + s.count('9') * 9)
# print(sum(map(int, s)))