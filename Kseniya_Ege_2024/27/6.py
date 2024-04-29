l = [int(x) for x in open('6.txt')]
#Найдите среди них подпоследовательность с
# максимальной суммой, кратной 43, определите её длину.
mx_sm = 0
ln = 0

for i in range(len(l) - 1):
    sm = 0
    for j in range(i, len(l)):
        sm += l[j]
        if sm % 43 == 0:
            if sm > mx_sm:
                mx_sm = sm
                ln = j - i + 1
print(ln)