li = [sorted([int(d) for d in x.split()]) for x in open('5.txt')]
ans = 0
for i in li:
    if len(set(i)) == 6:
        if (i[0] + i[-1]) / 2 < (sum(i) - i[0] - i[-1]) / 4:
            ans += 1
print(ans)