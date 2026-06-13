l = sorted([[int(d) for d in x.split()] for x in open('19.txt')])
yach = [[0, 0]] * 200
# yach[0] = [20, 150]
# print(yach)8
# for y in range(2):
#     yach.append([])
ct_otr = 0
mxmx = 0
for x in l:
    for y in range(len(yach)):
        if x[0] > yach[y][1]:
            yach[y] = x
            break
    mx1 = 0
    mn2 = 10 ** 7
    for y in yach:
        mx1 = max(mx1, y[0])
        mn2 = min(mn2, y[1])
    mxmx = max(mxmx, mn2 - mx1 + 1)
    if mn2 - mx1 + 1 < 0:
        ct_otr += 1
print(mxmx, ct_otr + 1)
print(mxmx, len(l) - ct_otr)
# Разобрать