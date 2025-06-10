import time
l = [int(x) for x in open('1.txt')]
start = time.time() #1980
print(start)
#print(l)
mx = []
ct = 0
#поиндексовый перебор
sr = sum(l) / len(l)
for x in range(len(l) - 1):
    #sum(l) сложность O(n) - линейная
    if l[x] < sr and l[x + 1] < sr:
        if str(l[x])[-1] == '9' or str(l[x + 1])[-1] == '9':
            mx.append(l[x] + l[x + 1])
            ct += 1
print(ct, max(mx))
#Алгоритмы и структуры данных
#Асимптотическая сложность. Асимптотика. Большая О
finish = time.time() #1980
print(finish - start)

#поэлементный перебор
# for x in l:
#     print(x, x + 1)
