# d = 5 # int
# print(d + 2)
# print(d - 10)
# print(d / 7)
# print(d * 9)
# print(d ** 3)
# print(d // 3)
# print()
# print(9 // 5)
# print(12 // 5)
# print(4 % 3)
# print(8 % 4)
# print(9 % 5)
# print(12 % 5)
# d = '59' # str
# print(d + '1')
# d = '1231231920317231'
# print(len(d))
# d = 5921371238712939312390123710128941268912462148216412784612478124612487125412847212
# print(len(str(d)))
#d = 59
#print(int(str(d)[0]) * int(str(d)[1]))
#print('5' * 10)
#print('5' + 10)
# d = input()
# print(d + '3')
# d = int(input())
# print(d + 3) # int числа str строки
# g = int(input())
# print(g + '2')
# print(g, str(g))
# d = 0  # if else elif
# if d > 0:
#     print('Число положительное')
# elif d < 0:
#     print('Число отрицательное')
# else:
#     print('Число равно нулю!')
# d = 2
# for x in range(2):
#     g = int(input())
#     d += g
# print(d)
# d = 14
# for x in range(4):
#     d -= 2
# print(d)
# d =0
# for x in range(3):
#     g = int(input())
#     if g < 0:
#         d += g
# print(d)
# a = int(input())
# s = 0
# for x in range(a):
#     s += 10
# print(s)
# a = int(input())
# s = 0
# for x in range(a):
#     s += int(input())
# print(s)
# a = int(input())
# s = a
# for x in range(a):
#     s += int(input())
# print(s)
# a = int(input())
# s = a + 1 # 4 + 2 + 3 + 4 =
# for x in range(a):
#     s += int(input()) + 1
# print(s)
# a = int(input())
# s = a - 1
# for x in range(a):
#     g = int(input())
#     if g > 2:
#         s += g
# print(s)
# d = 5
# while d > 0:
#     print('Привет!')
#     d -= 1
# d = -1
# s = 0
# while d != 0:
#     d = int(input())
#     s += d
# print(s)
d = -1
s = 0
while d != 0:
    d = int(input())
    if len(str(d)) == 2:
        s += d
print(s)