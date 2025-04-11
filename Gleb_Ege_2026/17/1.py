import time
start = time.time()
l = [int(x) for x in open('1.txt')]
mx = []
sr = sum(l) / len(l) #O(n)
for x in range(len(l) - 1):
    if l[x] < sr and l[x + 1] < sr:
        if str(l[x])[-1] == '9' or str(l[x + 1])[-1] == '9':
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))
# for x in range(len(l) - 1):
#     if l[x] < (sum(l) / len(l)) and l[x + 1] < (sum(l) / len(l)):
#         if str(l[x])[-1] == '9' or str(l[x + 1])[-1] == '9':
#             mx.append(l[x] + l[x + 1])
# print(len(mx), max(mx))
finish = time.time()
print((finish - start) * 100000)