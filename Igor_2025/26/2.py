l = sorted([int(x) for x in open('2.txt')])
i = 0
j = len(l) - 1
ct_korz = 0
while i < j:
    if l[i] + l[j] == 100:
        i += 1
        j -= 1
        ct_korz += 1
    elif l[i] + l[j] > 100:
        j -= 1
    else:
        i += 1
print(ct_korz)