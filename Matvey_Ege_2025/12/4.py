for i in range(10000):
    a = '3' + str(i*'9') + str(i*'5')
    while '39' in a or '35' in a or '555' in a:
        if '39' in a:
            a = a.replace('39', '55', 1)
        if '35' in a:
            a = a.replace('35', '9', 1)
        if '555' in a:
            a = a.replace('555', '3', 1)
    n = 0
    for j in a:
        n+=int(j)
    if n%len(a) == i:
        print(i)