for x in '0123456789ABCDEFGHIJKLMNOPQRSTUVWX':
    c1 = int( 'GP45' + x + '2', 34 )
    c2 = int( 'P7' + x, 34 )
    c3 = int( x + 'AI98', 34 )
    if ( c1 + (c2 * c3) ) % 13 == 0:
        print(x, ( c1 + (c2 * c3)) // 13 )