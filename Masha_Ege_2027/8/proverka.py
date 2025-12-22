import itertools
# ct = 0
# for x in itertools.product('ПИРОГ', repeat=4):
#     x = ''.join(x)
#     if x.count('О') <= 2:
#         if x.count('О') > 0 and 'ИО' not in x and 'ОО' not in x:
#             ct += 1
#         elif x.count('О') == 0:
#             ct += 1
# print(ct)
ct = 0
for x in itertools.product('012345678', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
        if x.count('6') == 1:
            if '26' not in x and '62' not in x and '36' not in x and '63' not in x and '46' not in x and '64' not in x and '56' not in x and '65' not in x:
                ct += 1
print(ct)