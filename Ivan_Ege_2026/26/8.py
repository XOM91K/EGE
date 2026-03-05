l = [[int(x) for x in d.split()] for d in open('8.txt')]
l = sorted(l)
points = [[0]*10 for i in range(10)]
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
print(sl)
mx_lines = []
for x in sl:
    sl[x] = sorted(set(sl[x]))
    ct = 1
    lines = 0
    for i in range(len(sl[x]) - 1):
        if sl[x][i + 1] - sl[x][i] == 1:
            ct += 1
            if ct == 5:
                lines += 1
                if lines == 9:
                    print(x)
        else:
            ct = 1
    mx_lines.append(lines)
print(max(mx_lines))

# for s in l:
#     points[s[0]-1][s[1]-1] = 1
# cl = []
# for st in points:
#     c = 0
#     is_going = 0
#     for i in range(len(st)-4):
#         if is_going==0:
#             if st[i]==st[i+1]==st[i+2]==st[i+3]==st[i+4]==1:
#                 is_going=1
#                 c += 1
#         else:
#             if st[i] == 0:
#                 is_going = 0
#     cl.append(c)
# maxx = max(cl)
# for i in range(len(cl)):
#     if cl[i] == maxx:
#         print(i+1)