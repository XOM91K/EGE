for n in range(2, 10000):
    r = bin(n)[2:]
    if r.count('0') == r.count('1'):
        r += r[-1]
    else:
        if r.count('1') > r.count('0'):
            r += '0'
        if r.count('1') < r.count('0'):
            r += '1'
    if r.count('0') == r.count('1'):
        r += r[-1]
    else:
        if r.count('1') > r.count('0'):
            r += '0'
        if r.count('1') < r.count('0'):
            r += '1'
    if r.count('0') == r.count('1'):
        r += r[-1]
    else:
        if r.count('1') > r.count('0'):
            r += '0'
        if r.count('1') < r.count('0'):
            r += '1'
    r = int(r, 2)
    if n > 154 and r % 7 == 0:
        print(r, n)