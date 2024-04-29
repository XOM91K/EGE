l = [int(x) for x in open('1.txt')]
n = l[0]
l = l[1:]
k = 5000
mx_ct = 0
for x in range(n - 1):
    sm = l[x]
    ct = 1
    for y in range(x + 1, n):
        sm += l[y]
        ct += 1
        if sm % k == 0:
            mx_ct = max(mx_ct, ct)
print(mx_ct)
print(l)