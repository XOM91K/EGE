from itertools import *
ct=0
for x in product('бандероль',repeat=7):
    x=''.join(x)
    if x.count('ь')<=1 :
        x = x.replace('б', '*')
        x = x.replace('н', '*')
        x = x.replace('д', '*')
        x = x.replace('р', '*')
        x = x.replace('л', '*')
        if 'е*' not in x and '*е' not in x:
            ct+=1
print(ct)
# бндрль
# 1877809
