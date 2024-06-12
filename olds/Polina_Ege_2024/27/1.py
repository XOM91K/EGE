t = 155
l = [int(x) for x in open('1.txt')]
mx_pr = 0
for i in range(len(l) - 2):
    for j in range(i + 1, len(l) - 1):
        for k in range(j + 1, len(l)):
            if abs(i - j) >= t and abs(j - k) >= t:
                mx_pr = max(mx_pr, l[i] * l[j] * l[k])
print(mx_pr)