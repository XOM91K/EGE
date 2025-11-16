l = [int(d) for d in open('11.txt')]
m = min([y for y in l if str(abs(y))[-1] == '4' and y > 0])
sm = []
for x in range(len(l)-2):
    if (sum(map(int, str(abs(l[x])))) + sum(map(int, str(abs(l[x + 1])))) + sum(map(int, str(abs(l[x + 2]))))) == m:
        sm.append(l[x] + l[x + 1] + l[x + 2])
print(len(sm), max(sm))