l = [int(x) for x in open('27.txt')]
l = sorted(l)
new_l = []
i = 0
j = len(l) - 1
ct = 0
sm = 0
while i < j: # 1 2 3 4 5 6 7 8 9
    new_l.append(l[i])
    sm += l[i]
    i += 1
    ct += 1
    if ct == 8 or ct % 9 == 0:
        new_l.append(l[j])
        j -= 1
        ct += 1

print(l)
print(new_l)
print(sm + l[j])