l = [int(x) for x in open('6.txt')]
mx = []
ct = 0
mn4 = min([x for x in l if str(x)[-1] == '4' and x > 0])
for x in range(len(l) - 2):
    if sum(map(int, str(abs(l[x])) + str(abs(l[x + 1])) + str(abs(l[x + 2])))) == mn4:
        ct += 1
        mx.append(sum([l[x], l[x + 1], l[x + 2]]))
print(ct, max(mx))