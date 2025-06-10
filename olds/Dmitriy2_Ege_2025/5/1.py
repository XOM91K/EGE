for x in range(100, 1000):
    x = str(x)
    c1 = int(x[0]) + int(x[1])
    c2 = int(x[1]) + int(x[2])
    itog_chislo = str(max(c1, c2)) + str(min(c1, c2))
    if itog_chislo == '1715':
        print(x)

#2 типа данных в Питоне:
int (целочисленный), str (строки)
d = 573
d = str(d)
print(d[2])
g = '876'
g = int(g)
print(g * 100)
x = 573 #12 #10
print(x + 2) # 575
d = "573"
print(d + '2') #5732
print(d * 2) #573573
x = 'Здравствуйте!\n'
print(x * 1000)

