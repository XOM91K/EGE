a=1
sum=0
while a != 0:
    a=int(input())
    if a % 3 == 0 and 1 <= a // 1 <= 9:
        sum += a
print(sum)