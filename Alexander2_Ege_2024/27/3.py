l = [int(x) for x in open('3.txt')]
k = 3
mx_sm = 0
for i in range(len(l) - 1):
    for j in range(i + k, len(l)):
        mx_sm = max(mx_sm, l[i] + l[j])
print(mx_sm)