l = [[int(d) for d in x.split()] for x in open('18.txt')]
l = sorted(l, key=lambda d: ((d[0] + d[-1]), d[0]))
arena_time = 0
z = []
for x in l:
    if x[0] >= arena_time:
        arena_time = x[0] + x[1]
        z.append(x)
print(len(z))
# for x in z:
#     print(x)
for x in l:
    if x[0] > 1384:
        print(x)