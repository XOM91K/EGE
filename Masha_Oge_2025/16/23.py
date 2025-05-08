import math
a = -1
sm = 0
while a != 0:
    a = int(input())
    if len(str(a)) == 3:
        if sum(map(int, str(a))) % 7 == 0:
            if math.prod(map(int, str(a))) > 30:
                sm += a
print(sm)

#
# a = 1273
# print(sum(map(int, str(a)))) # сумма цифр
# print(math.prod(map(int, str(a))))

# print(len(str(a)))