#Посчитать среднее арифметическое
#всех чисел из файла, которые не делятся на 5
# l = open('3.txt').readlines()
# print(l)
# print(int(l[0].strip()) + int(l[-1]))
l = open('3.txt').readlines()
s = []
for x in range(len(l)):
    l[x] = int(l[x])
    if l[x] % 5 != 0:
        s.append(l[x])
print(sum(s) / len(s))