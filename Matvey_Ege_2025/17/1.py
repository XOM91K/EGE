l = [int(x) for x in open('1.txt')]
sr = sum(l) / len(l)
ct_pair = 0
mx_pair = []
for x in range(len(l) - 1):
    if l[x] < sr and l[x + 1] < sr:
        if str(l[x])[-1] == '9' or str(l[x + 1])[-1] == '9':
            ct_pair += 1
            mx_pair.append(l[x] + l[x + 1])
print(ct_pair, max(mx_pair))
