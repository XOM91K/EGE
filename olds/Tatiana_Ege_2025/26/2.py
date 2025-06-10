l = [[int(d) for d in x.split()] for x in open('2.txt')]
#Задача из ЕГКР АПРЕЛЬ
l2 = []
for x in l:
    if x not in l2:
        l2.append(x)
l2 = sorted(l2)
l = l2.copy()
mx_ln = 1
ln = 1
for x in range(len(l) - 1):
    if l[x + 1][1] - l[x][1] == 2 and l[x][0] == l[x + 1][0]:
        ln += 1
        mx_ln = max(mx_ln, ln)
    else:
        ln = 1
for x in range(len(l) - 1):
    if l[x + 1][1] - l[x][1] == 2 and l[x][0] == l[x + 1][0]:
        ln += 1
        if ln == mx_ln:
            print(l[x][0])
            break
    else:
        ln = 1
print(mx_ln)