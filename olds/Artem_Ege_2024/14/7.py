for x in '0123456789abcdefghijklmnopqrs':
    for y in '0123456789abcdefghijklmnopqrs':
        c1=int('b'+'4'+'p'+'6r94e'+'p',30)
        c2=int('m'+'4'+'kgn'+'p',30)
        if (c1 + c2) % 10 == 0:
            print(x, (c1+c2)//10)