a = int(input())
l = []
for x in range(a):
    num = int(input())
    if num % 2 == 0:
        l.append(num)
print(min(l))