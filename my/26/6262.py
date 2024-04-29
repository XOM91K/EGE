l = sorted([int(x) for x in open('6262.txt')])
k = 6
sm = 100_000
korzina = [l[0]]
b = s = 0
last_money = 0
ct = 1
for x in range(1, len(l)):
    korzina.append(l[x])
    s = len(korzina) // k + (1 if len(korzina) % k == 0 else 0)
    b = len(korzina) - s
    if sm - (sum(korzina[-s:]) / 2 + sum(korzina[:b])) + last_money >= 0:
        sm -= (sum(korzina[-s:]) / 2 + sum(korzina[:b])) - last_money
        last_money = sum(korzina[-s:]) / 2 + sum(korzina[:b])
        ct += 1
    else:
        del korzina[-1]
        break
print(sm)
print(len(korzina))