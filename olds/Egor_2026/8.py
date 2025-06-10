a = 1
mx = -100
while a != -1 and a % 3 != 0:
    a = int(input())
    if -100 <= a <= 100:
        if a % 3 == 0 or abs(a) % 10 == 7:
            if a > mx:
                mx = a
print(mx)