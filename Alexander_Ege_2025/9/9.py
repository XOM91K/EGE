l = [sorted([int(d) for d in x.split()]) for x in open("9.txt")]
cnt = 0
for x in l:
    if len(set(x)) == 5:
        if (x[-1] + x[0]) / 2 == (x[1] + x[-2]) / 2 == x[2]:
            print(x)
            cnt += 1
print(cnt)
