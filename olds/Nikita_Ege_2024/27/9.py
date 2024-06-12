l = sorted([int(x) for x in open(r'C:\Users\Zarif\Downloads\27_B_9794 (1).txt')])
print(l)
s = 20138
i = 0
j = len(l) - 1
ct_pair = 0
while i < j:
    if l[i] + l[j] >= s:
        j -= 1
    else:
        i += 1
        ct_pair += len(l) - j - 1
print(ct_pair + ((len(l) - j) * (len(l) - j - 1) // 2))

#43666
# ct_pair = 0
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if l[i] + l[j] >= s:
#             ct_pair += 1
# print(ct_pair)