l = sorted([int(x) for x in open('2.txt')], reverse=True)
ct = 0
t = l[0]
for x in range(len(l) - 1):
    if t - l[x + 1] >= 3:
        t = l[x + 1]
        print(l[x + 1])
        ct += 1
print(ct + 1)