num = -1
sm = 0
while num != 0:
    num = int(input())
    if num == 0:
        break
    num = bin(num)[2:]
    if num == num[::-1]:
        sm += int(num, 2)
print(sm)
#15 7777