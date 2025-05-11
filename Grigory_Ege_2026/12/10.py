for n in range(1000):
    x = '>' + '0' * 17 + '3' * n + '2' * 17
    while '>3' in x or '>2' in x or '>0' in x:
        if '>3' in x:
            x = x.replace('>3', '22>', 1)
        if '>2' in x:
            x = x.replace('>2', '2>', 1)
        if '>0' in x:
            x = x.replace('>0', '3>', 1)
    print(n, x.count('2') * 2 + x.count('3') * 3)