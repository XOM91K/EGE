l = [int(x) for x in open('2.txt')]
sr = []
for x in l:
    if len(str(abs(x))) >= 2 and str(x)[-1] == str(x)[-2]:
        sr.append(x)
sr = sum(sr) / len(sr)
ct = 0
mx = 0
for x in range(len(l) - 1):
    if abs(l[x]) % 10 == abs(l[x + 1]) // 10 % 10 or abs(l[x + 1]) % 10 == abs(l[x]) // 10 % 10:
        if (abs(l[x]) % 11 == 0 and abs(l[x + 1]) % 11 != 0) or (abs(l[x + 1]) % 11 == 0 and abs(l[x]) % 11 != 0):
            if l[x] ** 2 + l[x + 1] ** 2 >= sr ** 2:
                ct += 1
                mx = max(mx, l[x] ** 2 + l[x + 1] ** 2)
print(ct, mx)