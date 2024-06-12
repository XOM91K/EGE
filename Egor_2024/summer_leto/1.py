x = int(input())
n = int(input())
flag = False
for i in range(n):
    a = int(input())
    if a == x:
        flag = True
if flag == False:
    print('ДА')
else:
    print('НЕТ')