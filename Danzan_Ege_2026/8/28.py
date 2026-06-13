def v14(d):
    s = []
    while d > 0:
        s.append(str(d%14))
        d //= 14
    return s[::-1]
ct = 0
for x in range(0, 1000000):
    x = v14(x)
    if len(x) == 5:
        nechet = [d for d in x if int(d) % 2 != 0]
        if len(nechet) == 2 and nechet[0] == nechet[1]:
            if abs(x.index(nechet[0]) - x[x.index(nechet[0]) + 1:].index(nechet[1])) + (x.index(nechet[0]) + 1) == 2:
                ct += 1
                print(x)
print(ct)