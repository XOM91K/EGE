for n in range( 1, 1000):
    s = '>' + '0' * 17 + '3' * n + '2' * 17
    while '>3' in s or '>2' in s or '>0' in s:
        if '>3' in s:
            s = s.replace( '>3', '22>', 1)
        if '>2' in s:
            s = s.replace( '>2', '2>', 1)
        if '>0' in s:
            s = s.replace( '>0', '3>', 1)
    s = s.replace( '>', '0')
    sm = sum(map(int, s)) ** 0.5
    if sm % 1 == 0:
        print(n, sm ** 2)