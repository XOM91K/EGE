l = [int(x) for x in open('3.txt')]
sm =[]
mn = min(l)
print(mn)
for x in range(len(l) - 1):
    if (l[x] % 77) * (l[x + 1] % 77) == mn ** 2:
        sm.append(l[x] * l[x + 1])
print(len(sm))
print(min(sm))