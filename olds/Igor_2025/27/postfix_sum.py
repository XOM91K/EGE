l = [2, 2, 1, 4, 8, 2, 1, 3]
pr_l = [0] * (len(l) + 1)
for i in range(len(l) - 1, -1, -1):
    pr_l[i] = pr_l[i + 1] + l[i]
print(l)
print(pr_l)