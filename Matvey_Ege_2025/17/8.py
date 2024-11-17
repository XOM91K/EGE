l = [int(x) for x in open('8.txt')]
ct = 0
c = []
mx = []
mn = [x for x in l if str(x)[-1:] == '4' and x > 0]
mn = min(mn)
for i in range(len(l) - 2):
    sum = 0
    for j in (str(abs(l[i])) + str(abs(l[i + 1])) + str(abs(l[i + 2]))):
        sum += int(j)
    if sum == mn:
        c.append(l[i] + l[i+1] + l[i+2])
        ct += 1
print(ct, max(c))