for n in range(1, 1000):
    s = '>2' + '12' * n + '<'
    while '>2<' not in s:
        if '>1' in s:
            s = s.replace('>1', '>2')
        if '>21' in s:
            s = s.replace('>21', '1>')
        if '12<' in s:
            s = s.replace('12<', '1<2')
        if '1<' in s:
            s = s.replace('1<', '<2')
    s = s.replace('>', '0')
    s = s.replace('<', '0')
    if sum(map(int, s)) > 103:
        print(n)
