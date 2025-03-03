l = [int(x) for x in open('5.txt')]
mn5 = []
mx = []
for x in l:
    if len(str(x)) == 3 and x % 10 == 5:
        mn5.append(x)
mn5 = min(mn5)
for x in range(len(l) - 1):
    if len(str(l[x])) == 3 or  len(str(l[x + 1])) == 3:
        if (l[x] + l[x + 1]) % mn5 == 0:
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))