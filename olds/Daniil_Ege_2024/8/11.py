import itertools
#99% - product для задач про числа
#ЕСТЬ ПОДВОХ -
ct = 0
for x in itertools.product('012345678', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('5') == 1 and '00' not in x and '11' not in x and '22' not in x and '33' not in x and '44' not in x and '55' not in x and '66' not in x and '77' not in x and '88' not in x and '99' not in x:
        ct += 1
        print(x)
print(ct)
#1337