l = sorted([int(x) for x in open('4.txt')])
s = 100
i = 0
j = len(l) - 1
ct = 0
while i < j:
    if l[i] + l[j] >= s:
        ct += 1

        i += 1
        j -= 1
    else:
        i += 1
        ct += 1
    ct += ct * (ct - 1) // 2
print(ct)
#43666
print(l)
# ct_pairs = 0
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if l[i] + l[j] >= s:
#             ct_pairs += 1
# print(ct_pairs)