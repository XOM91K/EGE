for n in range (2000):
    s ='3'*n
    ct = 0
    while '3333' in s or '222' in s:
        if '3333' in s:
            s =s.replace('3333','2',1)
        else:
            s = s.replace('222', '3', 1)
        ct += 1
    if s == '22' and ct == 34:
        print(n)