import itertools
count = 0
for i in itertools.product("0123456", repeat=6):
    i = "".join(i)
    if i[0] != "0" and int(i[-1]) >= 4:
        t1 = [j for j in i if j in "02468"]
        t2 = [j for j in i if j not in "02468"]
        if len(t1) == len(t2):
            count += 1
print(count)