import itertools
cnt=0
for x in set(itertools.permutations("АМФИБРАХИЙ", 10)):
    x="".join(x)
    if x[4]=="Б" and x[5]=="Р":
        cnt+=1
        print(x)
print(cnt)