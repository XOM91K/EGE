d = int(input())
mx = 0
for x in range(d):
    a = int(input())
    if a > 30000:
        print('Вы ввели число более 30.000')
        break
    if a > mx and a % 5 == 0:
        mx = a
print(mx)