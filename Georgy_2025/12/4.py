for n in range(10, 100):
    s = '1' + '0' * n
    while '10' in s:
        if '10' in s:
            s = s.replace('10', '001', 1)
        if '1' in s:
            s = s.replace('1', '01', 1)
    print(len(s))
    #РАЗОБРАТЬ