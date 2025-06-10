l = [[int(d) for d in g.split()] for g in open('1.txt')]
mx = 0
mn_rzn = 10 ** 10
for x in l:
    if abs(x[0] - x[1]) % 3 != 0:
        mn_rzn = min(mn_rzn, abs(x[0] - x[1]))
    mx += max(x)
if mx % 3 == 0:
    print(mx - mn_rzn)
else:
    print(mx)
