k=[]
for x in '123456789ABCDEFGHIJKLMNO':
    for y in range(1, 101):
      a=int(f'8AF7{x}11', 25)
      b=int(f'{x}DA87', 25)
      if (a+b)%y==0:
          k.append(y)
print(len(set(k)))