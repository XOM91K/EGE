a = int(input())
b = int(input())
c = int(input())
l = sorted([a, b, c])
print(l)
if a == b:
    print(a)
elif b == c:
    print(b)
else:
    print('Все числа разные')
