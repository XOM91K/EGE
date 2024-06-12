l = [int(x) for x in open('1.txt')]
mx_sm = 0
print(l)
k = 158
for i in range(len(l)):
    for j in range(i + k, len(l)):
        for r in range(j + k, len(l)):
            mx_sm = max(mx_sm, l[i] + l[j] + l[r])
print(mx_sm)