for n in range(1,1000):
    s = '>' + '0' * 12 + '1' * n + '2' * 8
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s=s.replace('>1', '22>',1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s=s.replace('>0', '1>',1)
    s = s.replace('>', '0')
    if sum([int(x) for x in s[:-1]]) ==68:
        print(n)