d = 5*3**1917 + 6*2**1878 + 7*3**1870 - 1991
s = []
while d > 0:
    s.append(d % 17)
    d //=17
print(s[::-1])
print(s[::-1].count(5))