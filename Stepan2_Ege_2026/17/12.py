l = [int(x) for x in open('12.txt')]
mn4 = min([d for d in l if str(abs(d))[-1] == '4' and d > 0])
mx = []
for x in range(len(l) - 2):
    if sum(map(int, str(abs(l[x])) + str(abs(l[x + 1])) + str(abs(l[x + 2])))) == mn4:
        mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))