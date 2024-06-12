l = sorted([int(x) for x in open('15.txt')], reverse=True)

ct = 1
mx_d = 0
i = 0
j = 1
while j != len(l):
    if (l[i] - l[j]) >= 8:
        ct += 1
        i = j
        mx_d = l[j]
    j += 1
print(ct, mx_d)