l = [int(x) for x in open('7.txt')]
mx_sm = 0
k = 166251
mx1 = mx2 = mx3 = 0
for i in range(len(l) - 2 * k):
    mx1 = max(mx1, l[i])
    mx2 = max(mx2, mx1 + l[i + k])
    mx3 = max(mx3, mx2 + l[i + 2 * k])
print(mx3)
# k = 158
# for i in range(len(l) - 2):
#     for j in range(i + k, len(l) - 1):
#         for t in range(j + k, len(l)):
#             mx_sm = max(mx_sm, l[i] + l[j] + l[t])
#print(mx_sm)