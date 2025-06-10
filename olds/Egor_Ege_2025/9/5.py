l = [sorted([int(d) for d in x.split()]) for x in open("5.txt")]
cnt = 0
for x in l:
    if x[-1] < x[0]+x[1]+x[2]:
        if x[0] + x[-1] == x[1] + x[2]:
                cnt += 1
print(cnt)