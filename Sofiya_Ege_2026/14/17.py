def f243(n):
    s=[]
    while n>0:
        s.append(n%243)
        n//=243
    return s
a=20*3**243+17*81**70+14*243**35+254-224*3**30
b=f243(a)
print(b)
print(b.count(2)+b.count(3)+b.count(5)+b.count(7)+b.count(11)+b.count(13)+b.count(17)+b.count(19))