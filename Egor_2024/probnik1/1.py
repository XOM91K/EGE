a = int(input())
b = int(input())
if a == b or abs(a) % 7 == 0 or abs(b) % 7 == 0 or (abs(a) % 10 == 2 and abs(b) % 10 == 2):
    print('Вариант 1')
elif (a % 3 == 0 and b % 3 == 0) or a % 10 == 2 or a % 10 == 2:
    print('Вариант 2')
else:
    print('Вариант 3')