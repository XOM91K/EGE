import itertools
ct = 0
for x in itertools.permutations("0123456789", r =7):
    x = "".join(x)
    if x[0]!="0":
        if int(x) % 5 == 0:
            x = x.replace("4", "2")
            x = x.replace("6", "2")
            x = x.replace("8", "2")
            x = x.replace("0", "2")
            x = x.replace("3", "1")
            x = x.replace("5", "1")
            x = x.replace("7", "1")
            x = x.replace("9", "1")
            if "22" not in x and "11" not in x:
                ct+=1
print(ct)