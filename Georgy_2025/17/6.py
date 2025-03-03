l = [int(x) for x in open('6.txt')]
mn4 = min([x for x in l if str(x)[-1] == '4' and x > 0])
ct = 0
mx = []
for x in range(len(l) - 2):
    st = str(abs(l[x])) + str(abs(l[x + 1])) + str(abs(l[x + 2]))
    if sum(map(int, st)) == mn4:
        ct += 1
        mx.append(l[x] + l[x + 1] + l[x + 2])
print(ct, max(mx))

# print(mn4)
# 123444556