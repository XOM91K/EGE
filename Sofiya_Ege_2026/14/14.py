for x in '0123456789ABCDEFGHIJKLMNOPQRSTUVW':
    a=int(f'GP45{x}2', 34)
    b=int(f'P7{x}', 34)
    c=int(f'{x}AI98', 34)
    if (a+b*c)%13==0:
        print((a+b*c)//13)