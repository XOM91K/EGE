l = sorted([int(x) for x in open('1.txt')])
ct = 0
ind = []
print(l)
i = 0
j = len(l) - 1
while j > i:
    if l[i] + l[j] == 100:
        ct += 1
        j -= 1
    elif l[i] + l[j] > 100:
        j -= 1
        i -= 1
    i += 1
print(ct)
# for x in range(len(l) - 1):
#     for y in range(x + 1, len(l)):
#         if l[x] + l[y] == 100 and x not in ind and y not in ind:
#             ct += 1
#             ind.append(y)
#             break
# print(ct)