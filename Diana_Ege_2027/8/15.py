import itertools
k=0
for x in itertools.product(sorted("СЕНТЯБРЬ"), repeat=5):
    x="".join(x)
    k+=1
    if k%2==0 and x[0]=="Р" and x.count("Ь")==0:
        print(k)