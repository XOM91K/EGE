def g(p ,s):
    if (p ==2 or p == 4) and s >=72:
        return True
    if p ==4 and s < 72:
        return False
    if p <4 and s >=72:
        return False
    if p % 2 == 0:
        return g(p + 1, s +3) and g(p + 1, s +5) and g(p + 1, s *2)
    else:
        return g(p + 1, s + 3) or g(p + 1, s + 5) or g(p + 1, s * 2)
for x in range(1,71):
    if g(0,x) ==True:
        print(x)