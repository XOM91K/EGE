r = [[int(d) for d in x.split()] for x in open('6.txt')]
l = r.copy()
l = sorted(l)
ct = 0
last_op = -1
op = [0 for x in range(500)]
for x in l:
    mn = 10 ** 10
    for y in range(len(op)):
        if x[0] > op[y]:
            op[y] = x[1]
            ct += 1
            last_op = y + 1
            break
        mn = min(mn, op[y])
    else:
        if x[1] > mn:
            last_op = op.index(mn) + 1
            op[op.index(mn)] = x[1]
            ct += 1
print(l)
print(op)
print(ct, last_op)
# for x in range(5):
#     print('hello')
# else:
#     print('yes')