# #№7C6443
# Сколько существует десятичных
# пятизначных чисел, в которых все цифры
# различны и никакие две чётные или две нечётные цифры не стоят рядом?
ct = 0
for x in range(10000, 100000):
    if len(set(str(x))) == 5:
        x = str(x)
        x = x.replace('2', '0')
        x = x.replace('4', '0')
        x = x.replace('6', '0')
        x = x.replace('8', '0')
        x = x.replace('3', '1')
        x = x.replace('5', '1')
        x = x.replace('7', '1')
        x = x.replace('9', '1')
        if '00' not in x and '11' not in x:
            ct += 1
print(ct)