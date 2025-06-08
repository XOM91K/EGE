for n in range(4,10000):
    s = '2'+n*'5'
    while '222' in s or '555' in s:
        if '555' in s:
            s =s.replace('555','2',1)
        else:
            s= s.replace('222','5',1)
    print(s.count('2')*2 + s.count('5')*5)