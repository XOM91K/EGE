for n in range(1, 10000):
    s = '>' + 12 * '0' + n * '1' + 8 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace ('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    s = s.replace('>', '')
    if sum(map(int, s)) == 68:
        print(n)