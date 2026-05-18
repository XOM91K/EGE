a = int(input()) # 5
b = int(input()) # 9
# 5 ** 2 + 7 ** 2 + 9 ** 2  = 25 + 49 + 81 = 155
sm = 0
for x in range(a, b + 1):
    if x % 2 == 1:
        sm += x ** 2
print(sm)
