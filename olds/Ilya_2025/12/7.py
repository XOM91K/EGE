mn = 10 ** 10
import itertools
for n in range(1, 20):
    for x in itertools.product('12', repeat=n):
        x = ''.join(x)
        if x.count('1') == x.count('2'):
            s = '0' + x + '0'
            while '00' not in s:
                if '011' in s:
                    s = s.replace('011', '101', 1)
                else:
                    s = s.replace('01', '40', 1)
                    s = s.replace('02', '20', 1)
                    s = s.replace('0222', '1401', 1)
            if s.count('1') == 6 and s.count('2') == 9:
                mn = min(mn, s.count('4'))
print(mn)