l = [int(x) for x in open('4.txt')]
l = sorted(l)
i = 0
j = len(l) - 1
cnt = 0
od = []
while i <= j:
    if l[i] + l[j] <= 400:
        cnt += 1
        i += 1
    elif l[i] + l[j] > 400:
        od.append(l[j])
    j -= 1
print(cnt, sum(od))