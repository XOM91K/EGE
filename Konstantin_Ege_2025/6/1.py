import turtle
turtle.lt(90)
turtle.tracer(0)
m=30
turtle.rt(90)
turtle.begin_fill()
for i in range(3):
    turtle.rt(45)
    turtle.fd(10*m)
    turtle.rt(45)
turtle.rt(315)
turtle.fd(10*m)
for i in range(2):
    turtle.rt(90)
    turtle.fd(10*m)
turtle.end_fill()
turtle.up()
ct = 0
for x in range(-50,50):
    for y in range(-50,50):
        t = turtle.getcanvas().find_overlapping(x * m, y * m, x * m, y * m)
        if len(t) == 1 and t[0] == 5:
            ct += 1
        turtle.goto(x*m,y*m)
        turtle.dot(3,"red")
print(ct)
turtle.done()
