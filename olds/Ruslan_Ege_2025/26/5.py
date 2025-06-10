l = [int(x) for x in open('5.txt')]
l = sorted(l)
i = 0
j = len(l) - 1
ct = 0
print(l[258], l[8061])
while i <= j:
    if l[i] + l[j] == 100:
        ct += 1
        i += 1
        j -= 1
    elif l[i] + l[j] > 100:
        j -= 1
    else:
        i += 1
print(ct)