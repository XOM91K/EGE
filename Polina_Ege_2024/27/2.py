k = 25
l = [int(x) for x in open('2.txt')]
mx_sm = 0
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if abs(i - j) >= k:
            mx_sm = max(mx_sm, l[i] + l[j])
print(mx_sm)