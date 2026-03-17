l = [[int(d) for d in x.split()] for x in open('6.txt')]
l = sorted(l)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
print(l)
print(sl)
for x in sl:
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 12:
            print(x, sl[x][y] + 1)
            break
# c = {'on': 222, 222:'two'}
# print(list(c.values()))
# print(list(c.keys()))
# print(list(c.items()))
# print(c['on'], c[222])
# for x in c:
#     print(x, c[x])
# print('two' in c)