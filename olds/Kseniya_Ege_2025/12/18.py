for n in range(1, 10000):
    s = '>' + 28 * '2' + n * '7' + 11 * '5'
    while '>5' in s or '>7' in s or '>2' in s:
        if '>5' in s:
            s = s.replace('>5', '77>', 1)
        if '>7' in s:
            s = s.replace('>7', '222>', 1)
        if '>2' in s:
            s = s.replace('>2', '55>', 1)
    s = s.replace('>', '0', 1)
    if sum(map(int, s)) > 1000 and sum(map(int, s)) % 20 == 0:
        print(n)