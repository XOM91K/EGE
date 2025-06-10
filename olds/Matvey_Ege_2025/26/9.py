l = [[int(d) for d in x.split()] for x in open('9.txt')]
# https://examinf.ru/tasks/416
b = []
for x in range(20):
    b.append([])
#
c = 0
i = 0
time_och = 0
print(l)
for x in l:
    for y in range(len(b)):
        if len(b[y]) == 0:
            c += 1
            b[y].append([x[0], x[0] + x[1]])
            break
        elif c == len(b):
            mn_time = 10 ** 10
            for z in range(len(b)):
                if b[z][-1][1] < mn_time:
                    mn_time = b[z][-1][1]
                    i = z
            time_och = max(time_och, mn_time - time_och)
            b[i].append([x[0], b[i][-1][1] + x[1]])
            if x[0] + x[1] < mn_time:
                mn_time = x[0] + x[1]
                i = y
            break
print(b)
print(max(b, key=len))