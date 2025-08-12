for n in range(1,1000):
    x = '>' + '0' * 39 + '1' * n + '2' * 39
    while '>1' in x or '>2' in x or '>0' in x :
        if '>1' in x :
            x= x.replace('>1','22>',1)
        if '>2' in x:
            x = x.replace('>2' , '2>' , 1)
        if '>0' in x:
            x = x.replace('>0' , '1>' , 1)
    print((x.count('1')*1 +x.count('2')*2),n)
