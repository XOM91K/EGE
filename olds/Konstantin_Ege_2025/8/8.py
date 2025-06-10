import itertools
k = 0
for x in itertools.permutations('ГЛУБИНА', 7):
   s = ''.join(x)
   if s.index('А') < s.index('И') < s.index('Г') or s.index('И') < s.index('А') < s.index('Г'):
       k += 1
print(k)
#АИГ
#ИАГ