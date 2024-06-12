# import itertools
# ct = 0
# for x in set(itertools.product('ЕВЛАМПИЙ', repeat=18)):
#     x = ''.join(x)
#     if x.count('Е') + x.count('А') + x.count('И') + x.count('Й') == x.count('В') + x.count('Л') + x.count('М') + x.count('П'):
#         if 'ПИЛАЕВЛА' in x[0:8]:
#             ct += 1
ct = 0
import itertools
ct = 0 # 'ПИЛАЕВЛАaaaaaaaaaa
for x in set(itertools.product('ЕВЛАМПИЙ', repeat=10)):
    x = ''.join(x)
    if x.count('Е') + x.count('А') + x.count('И') + x.count('Й') == x.count('В') + x.count('Л') + x.count(
        'М') + x.count('П'):
            ct += 1
print(ct)