for x in range(1,2006):
    d = 4**163 * 5 + 12**62 - x
    s  = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    if s.count('1') < s.count('4'):
        s = int(s,5)
        print(x)