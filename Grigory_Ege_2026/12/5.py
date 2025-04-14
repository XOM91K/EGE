for n in range(1,1000):
    x= '3'+'9'*n+'5'*n
    while '39' in x or '35' in x or '555' in x :
        if '39' in x:
            x=x.replace('39', '55',1)
        if '35' in x:
            x=x.replace('35', '9',1)
        if '555' in x:
            x=x.replace('555', '3',1)
    if (x.count('5')*5+x.count('9')*9+x.count('3')*3) % len(x) == n:
        print(n)