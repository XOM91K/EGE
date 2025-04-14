l = [int(x) for x in open('17.txt')]
mn4 = min([x for x in l if x > 0 and str(x)[-1] == '4'])
mx = []
for x in range(len(l) - 2):
    #3523 763 123
    if sum(map(int, str(abs(l[x])) + str(abs(l[x + 1])) + str(abs(l[x + 2])))) == mn4:
       mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))