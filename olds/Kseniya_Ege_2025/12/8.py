for n in range(1, 1000):
    s = '>2' + '12'*n + '<'
    while '>2<' not in s:
        s = s.replace('>1', '>2', 1)
        s = s.replace('>21', '1>', 1)
        s = s.replace('12<', '1<2', 1)
        s = s.replace('1<', '<2', 1)
    s = s.replace('<', '0', 1)
    s = s.replace('>', '0', 1)
    if sum(map(int, s)) > 103:
        print(n)