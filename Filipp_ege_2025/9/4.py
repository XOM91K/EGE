li = [sorted([int(d) for d in x.split()]) for x in open('4.txt')]
ans = 0
for i in li:
    if i[4] * i[4] > i[0] * i[1] * i[2] * i[3]:
        if i[4] + i[3] >= (i[0] + i[1] + i[2]) * 2:
            ans += 1
print(ans)