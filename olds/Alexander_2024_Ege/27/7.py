l = [int(x) for x in open('7.txt')]
k = 263
mx_ln = 0
for x in range(len(l) - 1):
    sm = 0
    for y in range(x, len(l)):
        sm += l[y]
        if sm % k == 0:
            mx_ln = max(mx_ln, y - x + 1)
print(mx_ln)