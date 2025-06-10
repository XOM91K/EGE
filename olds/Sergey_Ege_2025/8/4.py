import itertools
k = 0
for x in set(itertools.permutations("СПОРТЛОТО")):
     x = "".join(x)
     if "ТТ" in x:
         k += 1
         print(x)
print(k)