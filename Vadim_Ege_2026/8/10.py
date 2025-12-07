import itertools
c = 0

for x in set(itertools.product("СВЯТОСЛАВ", repeat = 7)):
    if x.count("Я")+x.count("О")+x.count("А") >= 4:
        c+=1
print(c)