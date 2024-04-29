# Определите количество пятизначных чисел,
# записанных в восьмеричной системе счисления,
# в записи которых только одна цифра 6, при
# этом никакая нечётная цифра не стоит рядом с цифрой 6.
import itertools
ct = 0
for x in itertools.product('01234567', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('6') == 1:
        if '16' not in x and '61' not in x and '36' not in x and '63' not in x and '56' not in x and '65' not in x and '76' not in x and '67' not in x:
            ct += 1
print(ct)