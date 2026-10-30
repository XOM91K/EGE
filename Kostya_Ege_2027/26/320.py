l = [int(x) for x in open('320.txt')]
l = sorted(l)
i = 0
j = len(l) - 1
cont = []
ct = 0
while i < j:
    if l[i] + l[j] <= 400:
        ct += 1
        i += 1
        j -= 1
    elif l[i] + l[j] > 400:
        cont.append(l[j])
        j -= 1

print(sum(cont))
print(ct)