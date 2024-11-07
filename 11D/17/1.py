l = [int(x) for x in open('1.txt')]
sr = sum(l) / len(l)
mx = 0
ct = 0
for x in range(len(l) - 1):
    if l[x] < sr and l[x + 1] < sr:
        if str(l[x])[-1] == '9' or str(l[x + 1])[-1] == '9':
            ct += 1
            mx = max(mx, l[x] + l[x + 1])
print(ct, mx)

# print(sr)
# # print(l)