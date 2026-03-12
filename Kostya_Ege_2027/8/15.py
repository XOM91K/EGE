import itertools
ct = 0
for x in itertools.product("01345678",repeat = 7):
    x = "".join(x)
    if len(set(x)) == 7 and x[0] != "0":
        x = x.replace("0","4")
        x = x.replace("6","4")
        x = x.replace("8","4")
        x = x.replace("3","1")
        x = x.replace("5","1")
        x = x.replace("7","1")
        if "11" not in x and "44" not in x:
            ct += 1
print(ct)