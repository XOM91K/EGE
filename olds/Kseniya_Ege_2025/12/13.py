for n in range(1, 10000):
    s = '>' + 17 * '0' + n * '3' + 17 * '2'
    while '>3' in s or '>2' in s or '>0' in s:
        if '>3' in s:
            s = s.replace('>3', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '3>', 1)

    #if  (s.count('>22') * 22 * s.count('2>') * 2 * s.count('>3') * 3) > 0:
    s = s.replace('>', '0')
    if sum(map(int, s)) ** 0.5 % 1 == 0:
        print(n)