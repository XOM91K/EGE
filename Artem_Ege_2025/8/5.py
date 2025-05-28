k =0
from itertools import *
for x in product(sorted('прога')[::-1], repeat=5):
  k += 1
  x = ''.join(x)
  if x.count('г')==2 and 'гг' not in x:
    if x[0]!='р':
      x = x.replace('а', 'о')
      if x.count('о')==0:
        print(k)
        break