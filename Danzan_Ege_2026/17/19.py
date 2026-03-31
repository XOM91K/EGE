l = [int(x) for x in open('19.txt')]
mx = []
ct = 0
for x in range(len(l) - 2):
    k = 0
    if str(l[x])[0] == str(l[x])[-1]:
        k += 1
    if str(l[x + 1])[0] == str(l[x + 1])[-1]:
        k += 1
    if str(l[x + 2])[0] == str(l[x + 2])[-1]:
        k += 1
    if k == 1:
        k5 = 0
        if len(str(abs(l[x]))) == 5 and str(l[x])[-4] == '7':
            k5 += 1
        if len(str(abs(l[x + 1]))) == 5 and str(l[x + 1]//1000)[-1] == '7':
            k5 += 1
        if len(str(abs(l[x + 2]))) == 5 and str(l[x + 2]//1000)[-1] == '7':
            k5 += 1
        if k5 == 2:
            ct += 1
            mx.append(max(l[x], l[x + 1], l[x + 2]))

print(ct, sum(mx))