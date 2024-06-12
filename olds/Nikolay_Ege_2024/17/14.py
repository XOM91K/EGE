l = [int(x) for x in open('14.txt')]
mx3 = 0
ct = 0
mx = 0
for x in l:
    if len(str(abs(x))) == 3 and str(abs(x))[-1] == '5':
        mx3 = max(mx3, x)
for x in range(len(l) - 2):
    if (str(abs(l[x]))[-1] == '5' and str(abs(l[x + 1]))[-1] != '5' and str(abs(l[x + 2]))[-1] != '5') \
        or (str(abs(l[x]))[-1] != '5' and str(abs(l[x + 1]))[-1] == '5' and str(abs(l[x + 2]))[-1] != '5') \
        or (str(abs(l[x]))[-1] != '5' and str(abs(l[x + 1]))[-1] != '5' and str(abs(l[x + 2]))[-1] == '5'):
        mx = max(mx, l[x] + l[x + 1], l[x + 2])
        ct += 1
print(ct, mx)