import itertools # iteration tools
# #permutations - перестановки
# #3! = 1 * 2 * 3 = 6
# #4! = 1 * 2 * 3 * 4 = 24
# for x in itertools.permutations('МГЛА', 4):
#     x = ''.join(x)
#     print(x)

#product - комбинации с повторениями букв
#ССС
#ССО
#ССН
#СОС
#СОО
#СОН
#3**3 = 27
#10**9 = 1.000.000.000
#1.000.000 = 1 секунда
# for x in itertools.product('СНОВЕДЕНИЕ', repeat=9):
#     x = ''.join(x)
#     print(x)