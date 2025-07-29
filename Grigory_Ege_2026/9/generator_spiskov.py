l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l)
s = [x for x in range(1, 11)]
print(s)
t = [0 for x in range(2, 5)]
print(t)
t = [0 for x in range(2, 3)]
print(t)
l = [x for x in range(0, 100, 2)]
print(l)
l = [x for x in range(0, 100) if x % 2 == 0 and x > 50]
print(l)

d = [5, 8, 3, 8, 8, 4, 4, 4, 4, 2, 2, 3, 6, 3]
t = [x for x in d if x % 3 == 0]
print(t)