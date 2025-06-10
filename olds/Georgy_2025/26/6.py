l = [[int(d) for d in x.split()] for x in open('6.txt')]
l = sorted(l)
mx_streak = 1
streak = 1
for x in range(len(l) - 1):
    if l[x][0] == l[x + 1][0] and l[x + 1][1] - l[x][1] == 0:
        continue
    if l[x][0] == l[x + 1][0] and l[x + 1][1] - l[x][1] == 1:
        streak += 1
        mx_streak = max(mx_streak, streak)
    else:
        streak = 1
for x in range(len(l) - 1):
    if l[x][0] == l[x + 1][0] and l[x + 1][1] - l[x][1] == 0:
        continue
    if l[x][0] == l[x + 1][0] and l[x + 1][1] - l[x][1] == 1:
        streak += 1
        if streak == mx_streak:
            print(l[x][0])
    else:
        streak = 1
print(mx_streak)