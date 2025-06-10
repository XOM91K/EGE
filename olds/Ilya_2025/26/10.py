l = [int(x) for x in open('10.txt')]
l = sorted(l)
i = 0
j = len(l) - 1
cnt = 0
sm = 0
while i < j:
    if l[i] + l[j] <= 400:
        cnt += 1
        i += 1
    else:
        sm += l[j]
    j -= 1
# [[100] [30]] <= 130
print(cnt, sm)