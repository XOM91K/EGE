for x in range(1, 10000):
    d = 9 ** 1942 + 9 * 6 ** 971 + 214 - x
    s = ''
    while d > 0:
        s += str( d % 9 )
        d //= 9
    s = s[::-1]
    if abs(s.count( '2' ) - s.count( '8' )) == 471:
        print(x)