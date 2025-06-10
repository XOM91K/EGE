l = [int(x) for x in open('4.txt')]
mn = min([x for x in l if x % 52 == 0])
itog = []
for x in range(len(l) - 2):
    if l[x] % 113 + l[x + 1] % 113 + l[x + 2] % 113 == mn:
        itog.append(l[x] + l[x + 1] + l[x + 2])
print(len(itog), max(itog))