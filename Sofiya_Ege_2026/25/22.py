def dels(d):
    l=[]
    for x in range(2, int(d**0.5)+1):
          if d%x==0:
              if x%10==7 and x != 7:
                  l.append(x)
              if (d // x)  % 10 == 7 and (d // x) != 7:
                  l.append(d//x)
    return sorted(set(l))
for x in range(1_125_000, 10**7):
    l=dels(x)
    if len(l) > 0:
        print(x, min(l))