import itertools
otv = 0
for x in itertools.product('12345670', repeat=6):
    x = ''.join(x)
    if x[0] != '0':
        if (max(int(x[0]),int(x[1])) < min(int(x[2]),int(x[3]),int(x[4]),int(x[5]))):
            x = x.replace('2', '0')
            x = x.replace('4', '0')
            x = x.replace('6', '0')
            if '000' not in x:
                otv += 1
                print(x)
print(otv)