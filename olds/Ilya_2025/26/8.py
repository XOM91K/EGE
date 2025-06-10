l = [int(x) for x in open('8.txt')]
l = sorted(l)
i = 0
j = len(l) - 1
ct = 0
while i < j:
    if l[i] + l[j] == 100:
        i += 1
        j -= 1
        ct += 1
    elif l[i] + l[j] < 100:
        i += 1
    else:
        j -= 1
print(ct)
# ct = 0
# ind = []
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if l[i] + l[j] == 100 and j not in ind and i not in ind:
#             ct += 1
#             ind.append(j)
#             break
# print(ct)