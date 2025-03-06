#a = open(r'11.txt').readlines()
#нужно обзятаельно считать через генератор списков
a = [int(x) for x in open('11.txt')]
ct=0
sr_arf  = sum([int(i) for i in a ])/len(a)
median = int(sorted(a)[len(a)//2])
#sorted(a) нельзя, потому что a - это список со строками,
# а не c int-ами, поэтому сортировка происходит символов как строк
#допустим строка "34" больше чем "19999999999999999" из-за того что первый символ первого числа имеет вес больший чем первый символ второго числа
print(sr_arf, median)
for i in range(len(a)):
    if sr_arf>median:
        if int(a[i])<=sr_arf and int(a[i])>=median:
            ct+=1
    if sr_arf < median:
        if int(a[i])>=sr_arf and int(a[i])<=median:
            ct+=1
print(ct)