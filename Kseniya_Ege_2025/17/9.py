l = [int(x) for x in open('9.txt')]
mn = min([x for x in l if str(x)[-1] == '4' and x > 0])
print(mn)
sm = []
for x in range(len(l) - 2):
    if sum(map(int, str(abs(l[x])) + str(abs(l[x + 1])) + str(abs(l[x + 2])))) == mn:
        sm.append(l[x] + l[x + 1] + l[x + 2])
print(len(sm), max(sm))