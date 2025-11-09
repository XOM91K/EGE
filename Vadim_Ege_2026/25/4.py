import fnmatch

def dels(x):
    l = []
    for d in range(2,int(x**0.5)+1):
        if x%d == 0:
          l.append(d)
          l.append(x//d)
    return sorted(set(l))
for x in range(23, 10**6, 23):
    if len(dels(x)) != 0:
        b = max(dels(x))
        if fnmatch.fnmatch(str(b),"*6215"):
            print(x,b)