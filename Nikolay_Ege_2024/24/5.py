s = open('5.txt').readlines()
ct = 0
for x in s:
    x = x.strip() #убирает \n в строке
    if x.count('YZ') > 1:
        ct += 1
print(ct)