import itertools
# # 4! = 1 * 2 * 3 * 4 = 24
# # permutations - перестановки, встречается примерно в 10% задачах
# for x in itertools.permutations('МГЛА', 4):
#     print(x)
# product - комбинации с повторениями букв - встречается в 90% задачах
# 4 ** 4 = 4 * 4 * 4 * 4 = 256
for x in itertools.product('МГЛА', repeat=4):
    # tuple
    x = ''.join(x)
    if 'ММ' not in x:
        print(x)