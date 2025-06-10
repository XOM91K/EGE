import itertools
k=0
for x in itertools.product(sorted("НОРМАЛЬЕ"),repeat=6):
    x="".join(x)
    k+=1
    if x=="НОРМАА":
        print(k,x)
# 137588
# 154817