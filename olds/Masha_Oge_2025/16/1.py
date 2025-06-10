#https://inf-oge.sdamgia.ru/problem?id=37867
a = 1
sm = 0
ct = 0
while a != 0:
    a = int(input())
    ct += 1
    if a % 3 == 0 and a % 10 == 8 and a <= 300:
        sm += a
    if ct == 100:
        print('Цикл завершен досрочно')
        print('Последнее введенное число:', a)
        break
print(sm, ct)