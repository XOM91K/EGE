l = [int(x) for x in open('4.txt')]
mnkv = min(l) ** 2
mn = []
for x in range(len(l) - 1):
    if (l[x] % 77) * (l[x + 1] % 77) == mnkv:
        mn.append(l[x] * l[x + 1])
print(mn)
print(len(mn), min(mn))