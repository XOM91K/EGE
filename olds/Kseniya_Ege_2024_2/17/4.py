l = [int(x) for x in open('4.txt')]
mx_35 = 0
mx_5 = 0
ct = 0
mx = 0
for x in l:
    if str(x)[-1] == '5' and str(x)[-2] == '3':
        mx_35 = max(mx_35, x)
for x in l:
    if str(x)[-1] == '5':
        mx_5 = max(mx_5, x)
for x in range(len(l) - 2):
    if (len(str(abs(l[x]))) == 4 and len(str(abs(l[x + 1]))) == 4 and len(str(abs(l[x + 2]))) != 4) or \
                (len(str(abs(l[x]))) != 4 and len(str(abs(l[x + 1]))) == 4 and len(str(abs(l[x + 2]))) == 4) or \
                (len(str(abs(l[x]))) == 4 and len(str(abs(l[x + 1]))) != 4 and len(str(abs(l[x + 2]))) == 4):
        if str(l[x])[-1] == '5' or str(l[x + 1])[-1] == '5' or str(l[x + 2])[-1] == '5':
            if (l[x] + l[x + 1] + l[x + 2]) > mx_35:
                ct += 1
                mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, abs(mx - mx_5))