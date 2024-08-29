l = [[int(d) for d in x.split()] for x in open('1.txt')]
mx_sm = 0
mn_r = 10 ** 10
for x in l:
    mx_sm += max(x)
    if abs(x[0] - x[1]) % 3 != 0:
        mn_r = min(mn_r, abs(x[0] - x[1]))
if mx_sm % 3 == 0:
    mx_sm -= mn_r
print(mx_sm)