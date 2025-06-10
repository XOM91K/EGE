l = sorted([int(x) for x in open('4.txt')], reverse=1)

#cakes = [[]]
cakes = [l[0]]
for x in l:
    if cakes[-1] - x >= 8:
        cakes.append(x)
print(len(cakes), cakes[-1])
# print(l)
#
# cnt = 1
#
# while cnt != 4314:
#     cake = []
#     for i in range(cnt, 4314):
#         if i == cnt:
#             cake.append(l[i])
#         elif cake[-1] - l[i] >= 8:
#             cake.append(l[i])
#     if len(cakes[0]) < len(cake):
#         cakes = []
#         cakes.append(cake)
#     elif len(cakes[0]) == len(cake):
#         cakes.append(cake)
#     cnt += 1
#
# print(len(cakes[0]), cakes[0][-1])  # Не пишу проверок самого большого последнего числа, ибо в списке всего-лишь 1 вариант самого крупного торта
