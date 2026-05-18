l = [int(x) for x in open('23.txt')]
mx = []
for x in range(len(l) - 2):
    k = 0
    if str(l[x])[0] == str(l[x])[-1]:
        k+=1
    if str(l[x + 1])[0] == str(l[x + 1])[-1]:
        k += 1
    if str(l[x + 2])[0] == str(l[x + 2])[-1]:
        k+=1
    if k == 1:
        ct = 0
        if len(str(l[x])) == 4 and str(l[x])[1] == '2':
            ct += 1
        if len(str(l[x + 1])) == 4 and str(l[x + 1])[1] == '2':
            ct += 1
        if len(str(l[x + 2])) == 4 and str(l[x + 2])[1] == '2':
            ct += 1
        if ct == 2:
            mx.append(max(l[x], l[x + 1], l[x + 2]))
print(len(mx), sum(mx))