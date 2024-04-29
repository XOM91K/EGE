l = [int(x) for x in open(r'C:\Users\Zarif\Downloads\2_1.txt')]
k = 1000000
l = sorted([[l[x], x] for x in range(len(l))])
print(l)