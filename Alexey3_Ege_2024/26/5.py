l = [[int(d) for d in x.split()] for x in open('5.txt')]
l = sorted(l)
mins = 1
old_mins = 1
ct_nab = 0
for x in range(len(l)):
    if mins == l[x][0] and old_mins == l[x][0]:
        mins = max(mins, l[x][1])
    else:
        ct_nab += 1
        mins =
print(l)