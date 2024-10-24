import random
l = [random.randint(10, 20) for x in range(5)]

for i in l:
    print(i, end=' ')
print()
for i in range(len(l)):
    print(l[i], end=' ')