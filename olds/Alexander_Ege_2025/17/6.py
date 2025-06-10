l = [int(x) for x in open('6.txt')]
mx_tr = []
mx17 = max([x for x in l if str(x)[-2:] == '17'])
for x in range(len(l) - 2):
    chet = [n for n in [l[x], l[x + 1], l[x + 2]] if len(str(n)) == 4]
    if len(chet) == 2:
        if l[x] % 5 == 0 or l[x + 1] % 5 == 0 or l[x + 2] % 5 == 0:
            if l[x] + l[x + 1] + l[x + 2] > mx17:
                mx_tr.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx_tr), max(mx_tr))