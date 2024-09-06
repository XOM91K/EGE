l = [2, 2, 1, 4, 8, 2, 1, 3]
pr_l = [0]
for i in range(len(l)):
    pr_l.append(pr_l[-1] + l[i])
print(l)
print(pr_l)