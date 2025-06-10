#296
import itertools
cnt=0
for w in itertools.product("КРЕМНИЙ", repeat=5):
    w="".join(w)
    if ("Е" in w or "И" in w) and ((w.count("Е") + w.count("И")) % 2 == 0) and w.count("Й")<=2:
        cnt+=1
        print(w)
        print(cnt)