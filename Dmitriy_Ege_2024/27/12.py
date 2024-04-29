l = [1, 3, 7, 10, 3, 2, 5, 7, 3, 4]
#    0  1  2  3   4  5  6  7  8  9
pr_l = [0] * (len(l) + 1)
for x in range(len(l)):
    pr_l[x + 1] = pr_l[x] + l[x]
print(pr_l)
i = 3
j = 5
print(pr_l[j + 1] - pr_l[i])
