d = 18*7**108 - 5*49**76 + 343**35 - 50
s =[]
d = abs(d)
while d>0:
    s.append(d % 49)
    d //=49
print(sum(s))