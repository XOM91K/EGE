import turtle as t
t.tracer(0)
t.lt(90)
m = 40
t.screensize(3000, 3000)
t.rt(90)
for n in range(8):
    t.fd(15 * m)
    t.rt(60)
    t.fd(10*m)
    t.rt(60)
t.up()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x *m, y*m)
        t.dot(3, 'red')

t.done()