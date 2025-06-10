#https://inf-oge.sdamgia.ru/problem?id=37885
a = 1
ct = 0
while a != 0:
    a = int(input())
    if 1 <= a // 100 <= 9 and a % 4 == 0 and a <= 30000:
        ct += 1
print(ct)