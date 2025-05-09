for n in range(1, 10000):
    s='>2' + '12'*n + '<'
    while '>2<' not in s:
        s=s.replace('>1', '>2', 1)
        s = s.replace('>21', '1>', 1)
        s = s.replace('12<', '1<2', 1)
        s = s.replace('1<', '<2', 1)
    s = s.replace('<', '0')
    s = s.replace('>', '0')
    if sum(map(int, s)) > 103:
        print(n)
        break