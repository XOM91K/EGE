s = 11023
l = [int(x) for x in open('3.txt')]
print(l)
ct = 0
i = 0
j = len(l) - 1
while i < j:
    if l[i] + l[j] >= s:
        j -= 1
        ct += 1
    else:
        i += 1
        ct += (len(l) - j - 1)
ct_right = ((len(l) - j - 1) * (len(l) - j - 2)) // 2
print(ct + ct_right)
# ct = 0
# print(l)
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if l[i] + l[j] >= s:
#             ct += 1
# print(ct)