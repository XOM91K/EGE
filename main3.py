from itertools import product
count = 0
for s in product("0123456789ABC", repeat = 6):
    if s.count("2") == 1 and s[0] != "0":
        if s.count("A") + s.count("B") + s.count("C")<=4:
            count += 1
print(count)