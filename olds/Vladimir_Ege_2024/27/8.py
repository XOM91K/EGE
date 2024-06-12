#12257 про высоту растений
l = [int(x) for x in open('8.txt')]
print(l)
mx_ln = 0
for i in range(len(l) - 1):
    sm = 0
    for j in range(i, len(l)):
        sm += l[j]
        if sm % 113 == 0:
            mx_ln = max(mx_ln, abs(i - j) + 1)
print(mx_ln)