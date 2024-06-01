l = [int(x) for x in open('3.txt')]
print(l)
sm = 0
mx_ct = 0
for i in range(len(l) - 1):
    sm = 0
    for j in range(i, len(l)):
        sm += l[j]
        if sm % 113 == 0:
            mx_ct = max(mx_ct, j - i + 1)
print(mx_ct)