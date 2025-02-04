l = [[int(d) for d in x.split()] for x in open('7.txt')]
cnt = 0
for x in l:
    ch = [g for g in x if g % 2 == 0]
    nch = [g for g in x if g % 2 != 0]
    k = 0
    if len(set(x)) == 4:
        k += 1
    if sum(nch) > sum(ch):
        k += 1
    if k == 1:
        print(x, nch, ch)
        cnt += 1
print(cnt)
# 29   511
#