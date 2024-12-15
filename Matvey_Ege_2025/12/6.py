for n in range(1, 100):
    c = '>' + '0' * 17 + '3' * n + '2' * 17
    while '>3' in c or '>2' in c or '>0' in c:
        if '>3' in c:
            c = c.replace('>3', '22>', 1)
        if '>2' in c:
            c = c.replace('>2', '2>', 1)
        if '>0' in c:
            c = c.replace('>0', '3>', 1)
    e = 0
    for i in c:
        if i in '1234567890':
            e += int(i)
    # if '.0' in str(e ** 0.5)[-2:]:
    if (e ** 0.5) % 1 == 0:
        print(n)