s = input()
s2 = list(map(int, s.split(' ')))
print(s2)
print(len(s2))
print(sum(s2) // len(s2))
g = list(map(lambda a: a * 2, s2))
print(g)
print(s2, g)
# 5 10 15 20
# 5101520