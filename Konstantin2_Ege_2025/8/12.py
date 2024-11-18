from itertools import product
k = 0
for i in product('0123456789ab', repeat=7):
    s = ''.join(i)
    if s.count('b') == 2 and s[0] != '0':
            s = s.replace('2','0').replace('4','0').replace('6','0').replace('8','0').replace('3','1').replace('5','1').replace('7', '1').replace('9','1').replace('a','0').replace('b','1')
            if '00' not in s and '11' not in s:
                k += 1
print(k)