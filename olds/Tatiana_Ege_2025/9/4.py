l = [[int(d) for d in x.split()] for x in open('4.txt')]
print(l)
# \n \r \t ' ' \f
# c = 0
# for i in l:
#     y1 = 0
#     y2 = 0
#     y3 = 0
#     if len(set(i)) == 3:
#         y1 += 1
#     if (i[3] + i[2]) / (i[0] + i[1]) > 2.0:
#         y2 += 1
#     if max(i) % min(i) != 0:
#         y3 += 1
#     if y1 == y2 == y3 == 1:
#         c += 1
# print(c)