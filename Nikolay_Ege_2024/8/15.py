from itertools import *
ct=0
for x in set(permutations('просто',6)):
    x=''.join(x)
    if 'пп' not in x and 'рр' not in x and 'cc' not in x and 'тт' not in x and 'оо' not in x:
        ct+=1
print(ct)