def is_prime(d):
    for x in range(2, d):
        if d % x == 0:
            return False
    return True
for n in range(0, 100):
    s = '>' + '0' * 39 + '1' * n + '2' * 39
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    s = s.replace('>', '0')
    if is_prime(sum(map(int, s))):
        print(n)