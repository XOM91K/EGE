for n in range(4, 10000):
    s = '2' + n * '7'
    while '27' in s or '777' in s or '377' in s:
        if '27' in s:
            s = s.replace('27', '7', 1)
        if '777' in s:
            s = s.replace('777', '3', 1)
        if '377' in s:
            s = s.replace('377', '72', 1)
    if  (2 ** s.count('2') * 3 ** s.count('3') * 7 ** s.count('7')) % 3 == 0 and str(2 ** s.count('2') * 3 ** s.count('3') * 7 ** s.count('7'))[-1] == '1':
        print(n)
#s = '2377'
#print(2 ** s.count('2') * 3 ** s.count('3') * 7 ** s.count('7'))