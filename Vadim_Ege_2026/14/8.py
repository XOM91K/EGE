def f(d):
    s = []
    while d > 0:
        s.append(d % 27)
        d //= 27
    return s[::-1]
c =  5*729**2024+3*243**1413-7*81**169-2*9**107+3017
c = f(c)
print(sum([x for x in c if x % 2 == 0 and x <= 25]))