l = [[int(d) for d in x.split()] for x in open('5.txt')]
l = sorted(l, key=lambda d: sum(d))
arena_time = 0
duels = []
for x in l:
    if x[0] >= arena_time:
        arena_time = sum(x)
        duels.append(x)
# for x in duels:
#     print(x)
for x in l:
    if x[0] > 1384:
        print(x)