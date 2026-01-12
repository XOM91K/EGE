c = 0
d = []
for x in range(1,10000):
  r = bin(x)[2:]
  if x%3==0:
    r = '1'+r[:-2]+'11'
  else:
    r = '10'+r+'0'
  if x%2==0 and int(r,2)>999:
    print(int(r,2))
    d.append(int(r, 2))
print(min(d))