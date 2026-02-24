import itertools
ct = 0
for x in itertools.product("123456789ABCDEF",repeat=6):
    x = "".join(x)
    x = x.replace("B", "A")
    x = x.replace("C", "A")
    x = x.replace("D", "A")
    x = x.replace("E", "A")
    x = x.replace("F", "A")
    if x[0] != "0":
        if x.count("A") <= 4:
            ct += 1
print(ct * 21)
