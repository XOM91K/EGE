for x in '0123456789ABCDEFGHIJKLMNOPQRST':
    for y in '0123456789ABCDEFGHIJKLMNOPQRST':
       a=int(f'B{y}{x}6R94E{x}',30)
       b=int(f'M{y}KGN{x}',30)
       if (a+b)%10==0:
           print(x, y,(a+b)//10)