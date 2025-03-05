for n in range(1, 100):
    s = '>' + '0' * 17 + '3' * n + '2' * 17
    while '>3' in s or ">2" in s or '>0' in s:
        if '>3' in s:
            s = s.replace('>3', '22>')
        if '>2' in s:
            s = s.replace('>2', '2>')
        if '>0' in s:
            s = s.replace('>0', '3>')
    s = s.replace('>', '')
    if sum(map(int, s)) ** 0.5 % 1 == 0:
        print(n)
