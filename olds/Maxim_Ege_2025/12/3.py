for k in range(0, 1000):
    s = '>' + '1' * 22 + '2' * k + '3' * 23
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        if '>2' in s:
            s = s.replace('>2', '21>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>', 1)
    if s.count('2') * 2 + s.count('1') > 2023:
        print(k)
        break