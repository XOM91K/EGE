for x in '0123456789ABCDEF':
    t = int('D'+'49'+x,16) + int('48'+'A'+'3'+x,16)
    if t %14==0:
        print(t//14)