l = [int(x) for x in open('4.txt')]
sr = sum(l) / len(l)
mx_pair = 0
ct = 0
for x in range(len(l) - 1):
    if l[x] > sr and l[x + 1] > sr and str(l[x] + l[x + 1])[-2:] == '31':
        ct += 1
        mx_pair = max(mx_pair, l[x] + l[x + 1])
print(ct, mx_pair)