def dels(d):
    l=[]
    for x in range(1, int(d**0.5)+1):
        if d%x==0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
for x in range(10000, 31623):
    x=x**2
    if x%2==0:
      l=dels(x)
      nch=[a for a in l if a%2!=0]
      if len(l)==39:
        print(x, max(nch))
100962304 24649
108826624 26569
114233344 27889
122589184 29929
131239936 32041
893292544 218089
939790336 229441
971444224 237169
976562500 244140625
987467776 241081
