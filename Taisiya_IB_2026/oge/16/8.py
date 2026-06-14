n = int(input())
l = []
for x in range(n):
    n1 = int(input())
    n2 = int(input())
    l.append(n1 * 60 + n2) # min(l) = 170
print(min(l) // 60, min(l) % 60)