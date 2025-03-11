l = [[int(d) for d in x.split()] for x in open('2.txt')]
ct = 0
for x in l:
    sm_nch = sum([d for d in x if d % 2 != 0])
    sm_ch = sum([d for d in x if d % 2 == 0])
    k = 0
    if len(set(x)) == 4:
        k += 1
    if sm_nch > sm_ch:
        k += 1
    if k == 1:
        ct += 1
print(ct)
# x = [1, 3, 5, 7, 9]
# sm_ch = [d for d in x if d % 2 == 0]
# print(sm_ch)