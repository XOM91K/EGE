# Задание ОГЭ 16. (Задача №863)
# https://examinf.ru/tasks/863
d = -1
sm = 0
while d != 0:
    d = int(input())
    if d == 0:
        break
    if len(str(d)) == 2 and d % 8 == 0:
        sm = sm + d
print(sm)
