l = [int(x) for x in open('7.txt')]
mx_ln = 0
for x in range(len(l) - 1):
    sm = 0
    for y in range(x, len(l)):
        sm += l[y]
        if sm % 137 == 0:
            mx_ln = max(mx_ln, abs(x - y) + 1)
print(mx_ln)

