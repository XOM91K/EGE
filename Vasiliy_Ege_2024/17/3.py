l = [int(x) for x in open('3.txt')]
mx_51 = 0
ct = 0
for x in l:
    if x % 51 == 0:
        mx_51 = max(mx_51, x)
mx = 0
for x in range(len(l) - 1):
    if ((l[x] > int(str(l[x])[-1]) * 51) and (l[x + 1] <= int(str(l[x + 1])[-1]) * 51)) or ((l[x + 1] > int(str(l[x + 1])[-1]) * 51) and (l[x] <= int(str(l[x])[-1]) * 51)):
        if l[x] + l[x + 1] < mx_51:
            ct += 1
            mx = max(mx, l[x] + l[x + 1])

print(ct, mx)
#print(l)