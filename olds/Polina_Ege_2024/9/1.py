l = [sorted([int(d) for d in x.split()]) for x in open('1.txt')]
ct = 0
for x in l:
    if (x[0] * x[1] * x[2]) % x[-1] == 0:
        ct += 1
        print(x)
print(ct)
#if (d[0] * d[1] * d[2] * d[3] / max(d)) % max(d) == 0
#Определите, какое количество четвёрок
# удовлетворяют условию, что наибольшее число
# является делителем произведения остальных.