#https://examinf.ru/tasks/389
l = [int(x) for x in open('3.txt')]
mn25 = min([i for i in l if str(i)[-2:] == '25']) ** 2
ct = 0
mx_pr = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k += 1
    if len(str(abs(l[x + 1]))) == 4:
        k += 1
    if len(str(abs(l[x + 2]))) == 4:
        k += 1
    if k >= 2:
        if l[x] * l[x + 1] * l[x + 2] <= mn25:
            ct += 1
            mx_pr.append(l[x] * l[x + 1] * l[x + 2])
print(ct, max(mx_pr))