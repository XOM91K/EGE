import itertools
k = 0
k1 = 0
otvet = 0
for x in itertools.product('0123456', repeat=6):
  x = ''.join(x)
  if x[0] != '0' and (x.count('0')+ x.count('2')+x.count('4')+x.count('6'))==(x.count('1')+ x.count('3')+x.count('5')):
    x = x.replace('1','0')
    x =x.replace('2','0')
    x = x.replace('3','0')
    if x[-1] != '0':
      otvet +=1
print(otvet)