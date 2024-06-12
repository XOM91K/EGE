l = [int(x) for x in open('5.txt')]
sr = []
ct = 0
mn = 10 ** 10
for x in l:
    if abs(x) % 100 == 28:
        sr.append(x)
sr = sum(sr) / len(sr)
for x in range(len(l) - 2):
    if len(str(abs(l[x]))) == 4 or len(str(abs(l[x + 1]))) == 4 or len(str(abs(l[x + 2]))) == 4:
        if (abs(l[x]) % 100 == 11 and abs(l[x + 1]) % 100 == 11 and abs(l[x + 2]) % 100 != 11) or (abs(l[x]) % 100 != 11 and abs(l[x + 1]) % 100 == 11 and abs(l[x + 2]) % 100 == 11) or (abs(l[x]) % 100 == 11 and abs(l[x + 1]) % 100 != 11 and abs(l[x + 2]) % 100 == 11):
            if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                ct += 1
                mn = min(mn, l[x] + l[x + 1] + l[x + 2])

print(ct, mn)