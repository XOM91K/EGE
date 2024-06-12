l = [int(x) for x in open('4.txt')]
ct = 0
mx = 0
for x in range(len(l) - 2):
    if l[x + 1] > 0 and str(l[x + 1])[-1] == '9':
        if not(l[x] > 0 and str(l[x])[-1] == '9'):
            if not(l[x + 2] > 0 and str(l[x + 2])[-1] == '9'):
                ct += 1
                mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)