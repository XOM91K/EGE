import itertools
ct=0
for x in set(itertools.permutations("АМФИБРАХИЙ",10)):
    x=''.join(x)
    if x.count("ИИФАА")>=1 or x.count("ААФИИ")>=1:
        ct+=1
print(ct)