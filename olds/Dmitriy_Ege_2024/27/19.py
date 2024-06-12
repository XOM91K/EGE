l = [int(x) for x in open('19.txt')]
k = 137
mx_sm = 0
mx_ln = 0
for x in range(len(l) - 1):
    sm = 0
    for y in range(x, len(l)):
        sm += l[y]
        if sm % k == 0:
            if sm >= mx_sm:
                mx_sm = sm
for x in range(len(l) - 1):
    sm = 0
    for y in range(x, len(l)):
        sm += l[y]
        if sm == mx_sm:
            print(y - x + 1)
print(mx_ln)