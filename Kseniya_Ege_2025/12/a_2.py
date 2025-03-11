import itertools
for x in range(5, 30):
    for s in itertools.product('12', repeat=x):
        s = ''.join(s)
        if s.count('1') == s.count('2'):
            while '00' not in s:
                if '011' in s:
                    s = s.replace('011', '101', 1)
                else:
                    s = s.replace('01', '40', 1)
                    s = s.replace('02', '20', 1)
                    s = s.replace('0222', '1401', 1)
            if s.count('1') == 6 and s.count('2') == 9:
                print(s.count('4'))