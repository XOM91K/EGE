l = [int(x) for x in open(r'C:\Users\Zarif\Downloads\27_B_8513.txt')]
for x in range(len(l)):
    l[x] = [l[x], x]
print(sorted(l))