l = [int(x) for x in open('6.txt')]
cnt = 0
mx = []
l_2 = min([y for y in l if len(str(abs(y))) == 2]) ** 2
l_4 = max([j for j in l if len(str(abs(j))) == 4 and str(j)[-1] == '1'])
for x in range(len(l) - 2):
    a = [i for i in [l[x], l[x+1], l[x+2]] if i > l_2]
    if len(a) == 2:
        if abs(l[x] * l[x+1] * l[x+2]) % l_4 == 0:
            cnt += 1
            mx.append(abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]))
print(cnt, max(mx))

print(10607+33206+18547)