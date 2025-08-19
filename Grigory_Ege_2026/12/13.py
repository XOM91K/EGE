for n in range (4,10000):
    x = '2'+'5'*n
    while '25' in x or '355' in x or '555' in x :
        if '25' in x :
            x = x.replace('25','5',1)
        if '355'in x :
            x = x.replace('355','522',1)
        if '555' in x :
            x = x.replace('555','3',1)
    if x.count('2') == 10:
        print(n)
        break