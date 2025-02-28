l = [[int(d) for d in x.split()] for x in open('23.txt')]
k = 0
for x in l:
    k += 1
    if x == sorted(x):
        ch_sm = [d for d in x if sum(map(int, str(d))) % 2 == 0 and x.count(d) > 1]
        if len(ch_sm) > 0:
            print(k, x)
# x = [1, 2, 3, 2]
# print(x)
# print(sorted(x))
# if x == sorted(x):
#     print('Отсортирован!')
# else:
#     print('Неотсортирован!')

# d = [34, 512, 942, 12]
# ch_sm = [x for x in d if sum(map(int, str(x))) % 2 == 0]
# print(ch_sm)