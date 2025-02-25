 #https://examinf.ru/tasks/299
import itertools
k=0
for x in itertools.product("ГАЛКТИ", repeat=8):
    x="".join(x)
    if (x[0]=="Г" or x[0]=="Л" or x[0]=="К" or x[0]=="Т") and (x[-1]=="А" or x[-1]=="И") and "КЛ" not in x:
        k+=1
        print(k)