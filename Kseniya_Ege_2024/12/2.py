for x in range(1, 10000000000):
    s = '0' + '1' * x + '2' * x + '0'
    while '00' not in s:
        s = s.replace('011', '20', 1)
        s = s.replace('022', '10', 1)
        s = s.replace('02', '110', 1)
        s = s.replace('01', '220', 1)
    if s.count('1') == 47 and s.count('2') < 70:
        print(x)