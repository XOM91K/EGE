l = [[int(d) for d in x.split()] for x in open('10.txt')]
#print(l)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx_nomber = 0
for x in sl:
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 12:
            mx_nomber = max(mx_nomber, x)
for x in sl:
    sl[x] = sorted(sl[x])
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 12:
            if x == mx_nomber:
                print(sl[x][y] + 1)
                break
print(mx_nomber)







#d = {'a': 555, 23: -9, 'hello':[1, 'hello', 'bye', -30]}
# for x in d:
#     print(x, d[x])
# d['a'] = 111

#
# print(l)