l = [int(x) for x in open('24.txt')]
ct = 0
mx = 0
mn4 = min([x for x in l if str(x)[-1] == '4' and x > 0])
for x in range(len(l) - 2):
    skl = str(abs(l[x])) + str(abs(l[x + 1])) + str(abs(l[x + 2]))
    skl = sum(map(int, skl))
    if skl == mn4:
        ct += 1
        mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)