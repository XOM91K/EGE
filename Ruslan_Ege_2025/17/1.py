l = [int(x) for x in open('1.txt')]
ct = 0
mn = min(l) #O(n)
mnp = []
# O(2 * n) = O(n)
# O(n ** 2)
for x in range(len(l) - 1): # O(n)
    if (l[x] % 77) * (l[x + 1] % 77) == mn ** 2: # O(1)
        print(l[x], l[x + 1])
        ct += 1
        mnp.append(l[x] * l[x + 1])
print(ct, min(mnp))

# for x in l: #поэлементный перебор
#     print(x, x + 1)
#print(l)