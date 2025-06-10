d = [6, 5, 4]
r = []
print(d)
for x in d:
    r.append(x % 2 == 0)
print(r)
print(all(r)) # ВСЕ значения TRUE  - то возвращает True