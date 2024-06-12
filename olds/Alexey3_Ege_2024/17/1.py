l = [int(x) for x in open('1.txt')]
mx17 = 0
for x in l:
    if len(str(abs(x))) == 5 and abs(x) % 100 == 17:
        mx17 = max(mx17, x)
ct = 0
mn = 10 ** 10
for x in range(len(l) - 2):
    if abs(l[x]) % 100 == 17 or abs(l[x + 1]) % 100 == 17 or abs(l[x + 2]) % 100 == 17:
        if abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]) <= mx17:
            ct += 1
            mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)