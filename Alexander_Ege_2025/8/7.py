# import itertools
# ct = 0
# # set() - функция, которая убирает дублирующие символы/слова
# # в слове СВЕТЛАНА - две одинаковые буквы "А", поэтому нужен set()
# for x in set(itertools.permutations('СВЕТЛАНА', 8)):
#     x = ''.join(x)
#     if 'АА' not in x:
#         print(x)
#         ct += 1
# print(ct)
# s = 'abracadabra'
# print(set(s))