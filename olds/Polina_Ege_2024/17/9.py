l = [int(x) for x in open('9.txt')]
mx_5 = 0
ct = 0
mx = 0
for x in l:
    if len(str(abs(x))) == 5 and abs(x) % 10 == 3:
        mx_5 = max(mx_5, x)
for x in range(len(l) - 2):
    if abs(l[x]) % 10 == 3 or abs(l[x + 1]) % 10 == 3 or abs(l[x + 2]) % 10 == 3:
        if l[x] + l[x + 1] + l[x + 2] <= mx_5:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)