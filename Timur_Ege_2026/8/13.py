import itertools

ct = 0
for x in itertools.product(sorted('ЗИМА'), repeat=5):
    x = ''.join(x)
    x = x.replace('З', '!')
    x = x.replace('М', '!')
    x = x.replace('И', '%')
    x = x.replace('А', '%')
    if x[0] == '!' and x[-1] == '%':
        ct += 1
print(ct)
