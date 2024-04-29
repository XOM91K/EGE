mx=0
for x in '0123456789ABCDEFGHIJ':
    for y in '0123456789ABCDEFGHIJ':
        c1=int(f'5{y}4{x}{y}4HJ4', 20)
        c2=int(f'4{y}6B{y}{x}1', 20)
        if (c1+c2)%15==0:
            c1 = int(f'584{x}84HJ4', 20)
            c2 = int(f'486B8{x}1', 20)
            print(x, c1+c2)