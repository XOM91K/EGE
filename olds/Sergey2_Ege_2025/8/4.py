import itertools
k = 0
ct = 0
for x in itertools.product('БЮУОФЦЖ', repeat=4):
   x = ''.join(x)
   k +=1
   if x[0] == 'Ж' and x[1] == 'О' and k % 2 == 0:
       print(k, x)
       ct += 1
print(ct)