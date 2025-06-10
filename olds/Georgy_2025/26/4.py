l = [[int(d) for d in x.split()] for x in open('4.txt')]
l = sorted(l)
l2 = []
for x in l:
    if x not in l2:
        l2.append(x)
l = l2.copy()
#print(l)
mx_streak = 1
streak = 1
for x in range(len(l) - 1):
    if l[x][0] == l[x + 1][0] and l[x + 1][1] - l[x][1] == 2:
        streak += 1
        mx_streak = max(mx_streak, streak)
    else:
        streak = 1
for x in range(len(l) - 1):
    if l[x][0] == l[x + 1][0] and l[x + 1][1] - l[x][1] == 2:
        streak += 1
        if streak == mx_streak:
            print(l[x][0])
    else:
        streak = 1
print(mx_streak)