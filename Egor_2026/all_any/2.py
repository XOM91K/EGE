d = [5, 5, 1]
r = []
print(d)
for x in d:
    r.append(x % 2 == 0)
print(r)
print(any(r)) #хотя бы одно значение True - то возвращает True