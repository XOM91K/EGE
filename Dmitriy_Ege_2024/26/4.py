l = sorted([int(x) for x in open('4.txt')], reverse=True)
i = 0
j = 1
ct = 1
mx_dl = 0
while j != len(l) - 1:
    if l[i] - l[j] >= 3:
        ct += 1
        i = j
        print(l[j])
    j += 1
print(ct, mx_dl)