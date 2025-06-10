l = []
for n in range(4,10000):
     s = "2" + "5"*n
     while "222" in s  or "555" in s:
          if "555" in s:
               s = s.replace("555","2",1)
          else:
               s = s.replace("222","5",1)
     l.append(sum(map(int,s)))
print(max(l))