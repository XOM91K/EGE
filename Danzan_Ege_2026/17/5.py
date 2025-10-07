l = [int(x) for x in open('5.txt')]
mx = []
min4 = [x for x in l if str(x)[-1] == '4' and x > 0]
for x in range(len(l) - 2):
    if sum(map(int, str(abs(l[x])) + str(abs(l[x + 1])) + str(abs(l[x + 2])))) == min(min4):
        mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))