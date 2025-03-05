numbers = list(map(int, input().split()))
chet = []
nechet = []
for x in numbers:
    if x % 2 == 0:
        chet.append(x)
    else:
        nechet.append(x)
print('Четные:', chet)
print('Нечетные:', nechet)