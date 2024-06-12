s = input().split()
n = int(s[0])
x = int(s[1])
y = int(s[2])
d = x ** y
clc = d % 10 ** n
lft = d // 10 ** n
while lft != 0:
    clc += lft % 10 ** n
    lft = lft // 10 ** n
print(clc)