l = [int(x) for x in open('4.txt')]
ct = 0
mx = 0
for x in range(len(l) - 1):
    for y in range(x + 1, len(l)):
        if abs(x - y) == 3:
            if (str(l[x])[-2:] == '13' and str(l[y])[-2:] != '13') and (str(l[x])[-2:] != '13' and str(l[y])[-2:] == '13'):
                ct += 1
                mx = max(mx, l[x] + l[y])
print(ct, mx)
#1, 2, 3, 4