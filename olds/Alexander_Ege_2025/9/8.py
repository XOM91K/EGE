#https://examinf.ru/tasks/145
l = [sorted([int(d) for d in x.split()]) for x in open('8.txt')]
cnt = 0
for x in l:
    if x[-1] ** 2 > x[0] * x[1] * x[2] * x[3]:
        if x[-1] + x[-2] > 2 * (x[0] + x[1] + x[2]):
            cnt += 1
print(cnt)