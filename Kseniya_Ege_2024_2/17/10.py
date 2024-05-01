l = [int(x) for x in open('10.txt')]
mx_3 = []
mx = []
ct = 0
for x in l:
    if abs(x) % 10 == 5 and len(str(abs(x))) == 3:
        mx_3.append(x)
mx_3 = max(mx_3)
for x in range(len(l) - 2):
    if (abs(l[x]) % 10 == 5 and abs(l[x + 1]) % 10 != 5 and abs(l[x + 2]) % 10 != 5) \
        or (abs(l[x]) % 10 != 5 and abs(l[x + 1]) % 10 == 5 and abs(l[x + 2]) % 10 != 5) \
        or (abs(l[x]) % 10 != 5 and abs(l[x + 1]) % 10 != 5 and abs(l[x + 2]) % 10 == 5):
        if (l[x] + l[x + 1] + l[x + 2]) <= mx_3:
            ct += 1
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(ct, max(mx))