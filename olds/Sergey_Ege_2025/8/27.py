import itertools

ct = 0
for x in itertools.product("0123456789AB", repeat=5):
    x = "".join(x)
    if x[0] != "0" and x.count("3") == 1:
        x = x.replace("0", "2")
        x = x.replace("4", "2")
        x = x.replace("6", "2")
        x = x.replace("4", "2")
        x = x.replace("8", "2")
        x = x.replace("A", "2")
        x = x.replace("3", "1")
        x = x.replace("5", "1")
        x = x.replace("7", "1")
        x = x.replace("9", "1")
        x = x.replace("B", "1")
        if "11" not in x and "22" not in x:
            ct += 1

print(ct)