l = [[int(d) for d in x.split()] for x in open('6.txt')]
l = sorted(l)
op = [0 for x in range(2)]
for x in l:
    mn = 10 ** 10
    for y in range(len(op)):
        if x[0] > op[y]:
            op[y] = x[1]
            break
        mn = op[y]
    else:
        op[op.index(mn)] = x[1]
print(l)
print(op)
# for x in range(5):
#     print('hello')
# else:
#     print('yes')