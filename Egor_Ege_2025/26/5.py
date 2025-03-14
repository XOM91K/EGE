l = [int(x) for x in open('5.txt')]
l = sorted(l)
i = 0
j = len(l) - 1
ct = 0
sm = 0
while i < j:
    if l[i] + l[j] <= 400:
        ct += 1
        i += 1
    else:
        sm += l[j]
    j -= 1
print(ct, sm)