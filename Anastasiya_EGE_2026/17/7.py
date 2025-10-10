l = [int(x) for x in open('7.txt')]
mn4 = min([x for x in l if str(x)[-1] == '4' and x > 0])
mx = []
for x in range(len(l) - 2):
    c = str(abs(l[x])) + str(abs(l[x + 1])) + str(abs(l[x + 2]))
    c = sum(map(int, c))
    if c == mn4:
        mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))