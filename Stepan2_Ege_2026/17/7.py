l = [int(x) for x in open('7.txt')]
kr41 = min([d for d in l if (abs(d)) % 41 == 0 and d > 0])
# print(kr41)
mx = []
for x in range(len(l) - 1):
    if l[x] != l[x + 1]:
        if abs((l[x]) - (l[x + 1])) % kr41 == 0:
            mx.append((l[x]) + (l[x + 1]))
print(len(mx), max(mx))