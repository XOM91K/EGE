from turtle import *
tracer(0)
c = 20
bk(5*c)
lt(90)
bk(8*c)
down()
for i in range(2):
    fd(13 * c)
    rt(90)
    fd(20*c)
    rt(90)
up()
fd(8*c)
rt(90)
bk(3*c)
lt(90)
down()
for i in range(2):
    fd(16 * c)
    rt(90)
    fd(8*c)
    rt(90)
up()
for x in range(-c,c):
    for y in range(-c,c):
        goto(x*c,y*c)
        dot(3)
done()