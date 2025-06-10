# https://examinf.ru/tasks/143
l = [sorted([int(d) for d in x.split()]) for x in open("10.txt")]
# print(l)
cnt = 0
for x in l:
    if len(set(x)) == 3:
        if (x[-1] + x[-2]) > 2 * (x[0] + x[1]):
            if (x[-1] % x[0]) != 0:
                cnt += 1
print(cnt)
