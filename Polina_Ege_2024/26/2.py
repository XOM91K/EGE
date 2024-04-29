#2639 на полякове
k = 50
l = sorted([int(x) for x in open('2.txt')])
l = l[k:-k]
print(max(l), sum(l) // len(l))